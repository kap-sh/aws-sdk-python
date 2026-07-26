"""Generated from Smithy shape ``com.amazonaws.forecast#ListWhatIfForecastsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.next_token
    import capo_forecast.types.what_if_forecasts


class ListWhatIfForecastsResponse(TypedDict, closed=True):
    what_if_forecasts: NotRequired[
        "capo_forecast.types.what_if_forecasts.WhatIfForecasts"
    ]
    """<p>An array of <code>WhatIfForecasts</code> objects that describe the matched forecasts.</p>"""
    next_token: NotRequired["capo_forecast.types.next_token.NextToken"]
    """<p>If the result of the previous request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWhatIfForecastsResponse) -> dict:
    out: dict = {}
    if "what_if_forecasts" in value:
        import capo_forecast.types.what_if_forecasts

        out["WhatIfForecasts"] = (
            capo_forecast.types.what_if_forecasts.serialize_aws_json_1_1(
                value["what_if_forecasts"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWhatIfForecastsResponse:
    out: ListWhatIfForecastsResponse = {}  # type: ignore[typeddict-item]
    if "WhatIfForecasts" in data:
        import capo_forecast.types.what_if_forecasts

        out["what_if_forecasts"] = (
            capo_forecast.types.what_if_forecasts.deserialize_aws_json_1_1(
                data["WhatIfForecasts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
