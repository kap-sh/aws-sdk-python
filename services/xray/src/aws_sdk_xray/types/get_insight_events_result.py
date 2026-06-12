"""Generated from Smithy shape ``com.amazonaws.xray#GetInsightEventsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_xray.types.insight_event_list
    import aws_sdk_xray.types.token


class GetInsightEventsResult(TypedDict):
    insight_events: NotRequired[
        "aws_sdk_xray.types.insight_event_list.InsightEventList"
    ]
    """<p>A detailed description of the event. This includes the time of the event, client and root cause impact statistics, and the top anomalous service at the time of the event.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.token.Token"]
    """<p>Use this token to retrieve the next page of insight events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightEventsResult) -> dict:
    out: dict = {}
    if "insight_events" in value:
        import aws_sdk_xray.types.insight_event_list

        out["InsightEvents"] = aws_sdk_xray.types.insight_event_list.serialize_json(
            value["insight_events"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetInsightEventsResult:
    out: GetInsightEventsResult = {}  # type: ignore[typeddict-item]
    if "InsightEvents" in data:
        import aws_sdk_xray.types.insight_event_list

        out["insight_events"] = aws_sdk_xray.types.insight_event_list.deserialize_json(
            data["InsightEvents"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
