"""Generated from Smithy shape ``com.amazonaws.forecastquery#QueryWhatIfForecastResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecastquery.types.forecast


class QueryWhatIfForecastResponse(TypedDict):
    forecast: NotRequired["aws_sdk_forecastquery.types.forecast.Forecast"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryWhatIfForecastResponse) -> dict:
    out: dict = {}
    if "forecast" in value:
        import aws_sdk_forecastquery.types.forecast

        out["Forecast"] = aws_sdk_forecastquery.types.forecast.serialize_aws_json_1_1(
            value["forecast"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryWhatIfForecastResponse:
    out: QueryWhatIfForecastResponse = {}  # type: ignore[typeddict-item]
    if "Forecast" in data:
        import aws_sdk_forecastquery.types.forecast

        out["forecast"] = aws_sdk_forecastquery.types.forecast.deserialize_aws_json_1_1(
            data["Forecast"]
        )
    return out
