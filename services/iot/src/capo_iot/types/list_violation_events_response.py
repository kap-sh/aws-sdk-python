"""Generated from Smithy shape ``com.amazonaws.iot#ListViolationEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.next_token
    import capo_iot.types.violation_events


class ListViolationEventsResponse(TypedDict, closed=True):
    violation_events: NotRequired["capo_iot.types.violation_events.ViolationEvents"]
    """<p>The security profile violation alerts issued for this account during the given time period, potentially filtered by security profile, behavior violated, or thing (device) violating.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListViolationEventsResponse) -> dict:
    out: dict = {}
    if "violation_events" in value:
        import capo_iot.types.violation_events

        out["violationEvents"] = capo_iot.types.violation_events.serialize_json(
            value["violation_events"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListViolationEventsResponse:
    out: ListViolationEventsResponse = {}  # type: ignore[typeddict-item]
    if "violationEvents" in data:
        import capo_iot.types.violation_events

        out["violation_events"] = capo_iot.types.violation_events.deserialize_json(
            data["violationEvents"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
