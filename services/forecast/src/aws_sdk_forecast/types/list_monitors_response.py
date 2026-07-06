"""Generated from Smithy shape ``com.amazonaws.forecast#ListMonitorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.monitors
    import aws_sdk_forecast.types.next_token


class ListMonitorsResponse(TypedDict, closed=True):
    monitors: NotRequired["aws_sdk_forecast.types.monitors.Monitors"]
    """<p>An array of objects that summarize each monitor's properties.</p>"""
    next_token: NotRequired["aws_sdk_forecast.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Forecast returns this token. To retrieve the next set of results, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMonitorsResponse) -> dict:
    out: dict = {}
    if "monitors" in value:
        import aws_sdk_forecast.types.monitors

        out["Monitors"] = aws_sdk_forecast.types.monitors.serialize_aws_json_1_1(
            value["monitors"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMonitorsResponse:
    out: ListMonitorsResponse = {}  # type: ignore[typeddict-item]
    if "Monitors" in data:
        import aws_sdk_forecast.types.monitors

        out["monitors"] = aws_sdk_forecast.types.monitors.deserialize_aws_json_1_1(
            data["Monitors"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
