"""Generated from Smithy shape ``com.amazonaws.forecastquery#QueryWhatIfForecastResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecastquery.types.forecast


class QueryWhatIfForecastResponse(TypedDict, closed=True):
    forecast: NotRequired["capo_forecastquery.types.forecast.Forecast"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryWhatIfForecastResponse) -> dict:
    out: dict = {}
    if "forecast" in value:
        import capo_forecastquery.types.forecast

        out["Forecast"] = capo_forecastquery.types.forecast.serialize_aws_json_1_1(
            value["forecast"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryWhatIfForecastResponse:
    out: QueryWhatIfForecastResponse = {}  # type: ignore[typeddict-item]
    if "Forecast" in data:
        import capo_forecastquery.types.forecast

        out["forecast"] = capo_forecastquery.types.forecast.deserialize_aws_json_1_1(
            data["Forecast"]
        )
    return out
