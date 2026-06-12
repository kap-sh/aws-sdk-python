"""Generated from Smithy shape ``com.amazonaws.forecast#ListForecastsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.forecasts
    import aws_sdk_forecast.types.next_token


class ListForecastsResponse(TypedDict):
    forecasts: NotRequired["aws_sdk_forecast.types.forecasts.Forecasts"]
    """<p>An array of objects that summarize each forecast's properties.</p>"""
    next_token: NotRequired["aws_sdk_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListForecastsResponse) -> dict:
    out: dict = {}
    if "forecasts" in value:
        import aws_sdk_forecast.types.forecasts

        out["Forecasts"] = aws_sdk_forecast.types.forecasts.serialize_aws_json_1_1(
            value["forecasts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListForecastsResponse:
    out: ListForecastsResponse = {}  # type: ignore[typeddict-item]
    if "Forecasts" in data:
        import aws_sdk_forecast.types.forecasts

        out["forecasts"] = aws_sdk_forecast.types.forecasts.deserialize_aws_json_1_1(
            data["Forecasts"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
