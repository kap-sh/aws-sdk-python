"""Generated from Smithy shape ``com.amazonaws.forecast#ErrorMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.double
    import capo_forecast.types.forecast_type


class ErrorMetric(TypedDict, closed=True):
    forecast_type: NotRequired["capo_forecast.types.forecast_type.ForecastType"]
    """<p> The Forecast type used to compute WAPE, MAPE, MASE, and RMSE. </p>"""
    wape: NotRequired["capo_forecast.types.double.Double"]
    """<p> The weighted absolute percentage error (WAPE). </p>"""
    rmse: NotRequired["capo_forecast.types.double.Double"]
    """<p> The root-mean-square error (RMSE). </p>"""
    mase: NotRequired["capo_forecast.types.double.Double"]
    """<p>The Mean Absolute Scaled Error (MASE)</p>"""
    mape: NotRequired["capo_forecast.types.double.Double"]
    """<p>The Mean Absolute Percentage Error (MAPE)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorMetric) -> dict:
    out: dict = {}
    if "forecast_type" in value:
        out["ForecastType"] = value["forecast_type"]
    if "wape" in value:
        out["WAPE"] = value["wape"]
    if "rmse" in value:
        out["RMSE"] = value["rmse"]
    if "mase" in value:
        out["MASE"] = value["mase"]
    if "mape" in value:
        out["MAPE"] = value["mape"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorMetric:
    out: ErrorMetric = {}  # type: ignore[typeddict-item]
    if "ForecastType" in data:
        out["forecast_type"] = data["ForecastType"]
    if "WAPE" in data:
        out["wape"] = data["WAPE"]
    if "RMSE" in data:
        out["rmse"] = data["RMSE"]
    if "MASE" in data:
        out["mase"] = data["MASE"]
    if "MAPE" in data:
        out["mape"] = data["MAPE"]
    return out
