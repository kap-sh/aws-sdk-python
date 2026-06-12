"""Generated from Smithy shape ``com.amazonaws.iot#ListViolationEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.violation_events


class ListViolationEventsResponse(TypedDict):
    violation_events: NotRequired["aws_sdk_iot.types.violation_events.ViolationEvents"]
    """<p>The security profile violation alerts issued for this account during the given time period, potentially filtered by security profile, behavior violated, or thing (device) violating.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListViolationEventsResponse) -> dict:
    out: dict = {}
    if "violation_events" in value:
        import aws_sdk_iot.types.violation_events

        out["violationEvents"] = aws_sdk_iot.types.violation_events.serialize_json(
            value["violation_events"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListViolationEventsResponse:
    out: ListViolationEventsResponse = {}  # type: ignore[typeddict-item]
    if "violationEvents" in data:
        import aws_sdk_iot.types.violation_events

        out["violation_events"] = aws_sdk_iot.types.violation_events.deserialize_json(
            data["violationEvents"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
