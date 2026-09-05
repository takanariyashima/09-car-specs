"""
車種スペックAPI。

- /cars: 車名(make/model)で検索し、エンジン・馬力・年式を返す(内部データ)
- /vin/{vin}: VINの先頭3桁(WMI)からメーカー・生産国のみを判定する
  (詳細スペックまでのVINデコードには各社非公開の有料データベースが必要なため、
  本APIでは公開規格の範囲=メーカー/生産国の判定に留める)
"""

from typing import Optional

from fastapi import FastAPI, Query

from data import CARS, WMI_TABLE

app = FastAPI(
    title="Car Specs API",
    description="車種名からスペックを検索、VINからメーカー・生産国を判定します。",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"status": "ok", "service": "car-specs"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/cars")
def list_cars(
    make: Optional[str] = Query(None, description="メーカー名の部分一致検索"),
    model: Optional[str] = Query(None, description="車種名の部分一致検索"),
):
    results = CARS
    if make:
        m = make.lower()
        results = [c for c in results if m in c["make"].lower()]
    if model:
        mo = model.lower()
        results = [c for c in results if mo in c["model"].lower()]
    return {"count": len(results), "results": results}


@app.get("/vin/{vin}")
def decode_vin(vin: str):
    vin = vin.upper().strip()
    if len(vin) != 17:
        return {"valid": False, "reason": f"VINは17桁である必要があります(入力は{len(vin)}桁)"}

    wmi = vin[:3]
    info = WMI_TABLE.get(wmi)
    if not info:
        return {
            "valid": True,
            "wmi": wmi,
            "manufacturer": None,
            "country": None,
            "note": "このWMIは内部テーブルに未登録です(主要メーカーのみ対応)",
        }

    return {
        "valid": True,
        "wmi": wmi,
        "manufacturer": info["manufacturer"],
        "country": info["country"],
        "note": "VINから判定できるのはメーカー・生産国まで。詳細スペックは車名で /cars を検索してください。",
    }
