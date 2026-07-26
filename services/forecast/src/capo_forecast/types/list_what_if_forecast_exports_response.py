"""Generated from Smithy shape ``com.amazonaws.forecast#ListWhatIfForecastExportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.next_token
    import capo_forecast.types.what_if_forecast_exports


class ListWhatIfForecastExportsResponse(TypedDict, closed=True):
    what_if_forecast_exports: NotRequired[
        "capo_forecast.types.what_if_forecast_exports.WhatIfForecastExports"
    ]
    """<p>An array of <code>WhatIfForecastExports</code> objects that describe the matched forecast exports.</p>"""
    next_token: NotRequired["capo_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Forecast returns this token. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWhatIfForecastExportsResponse) -> dict:
    out: dict = {}
    if "what_if_forecast_exports" in value:
        import capo_forecast.types.what_if_forecast_exports

        out["WhatIfForecastExports"] = (
            capo_forecast.types.what_if_forecast_exports.serialize_aws_json_1_1(
                value["what_if_forecast_exports"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWhatIfForecastExportsResponse:
    out: ListWhatIfForecastExportsResponse = {}  # type: ignore[typeddict-item]
    if "WhatIfForecastExports" in data:
        import capo_forecast.types.what_if_forecast_exports

        out["what_if_forecast_exports"] = (
            capo_forecast.types.what_if_forecast_exports.deserialize_aws_json_1_1(
                data["WhatIfForecastExports"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
