"""Generated from Smithy shape ``com.amazonaws.forecast#ListForecastsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.forecasts
    import capo_forecast.types.next_token


class ListForecastsResponse(TypedDict, closed=True):
    forecasts: NotRequired["capo_forecast.types.forecasts.Forecasts"]
    """<p>An array of objects that summarize each forecast's properties.</p>"""
    next_token: NotRequired["capo_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListForecastsResponse) -> dict:
    out: dict = {}
    if "forecasts" in value:
        import capo_forecast.types.forecasts

        out["Forecasts"] = capo_forecast.types.forecasts.serialize_aws_json_1_1(
            value["forecasts"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListForecastsResponse:
    out: ListForecastsResponse = {}  # type: ignore[typeddict-item]
    if "Forecasts" in data:
        import capo_forecast.types.forecasts

        out["forecasts"] = capo_forecast.types.forecasts.deserialize_aws_json_1_1(
            data["Forecasts"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
