"""Generated from Smithy shape ``com.amazonaws.ssm#GetCalendarStateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.calendar_state
    import aws_sdk_ssm.types.iso8601_string


class GetCalendarStateResponse(TypedDict):
    state: NotRequired["aws_sdk_ssm.types.calendar_state.CalendarState"]
    """<p>The state of the calendar. An <code>OPEN</code> calendar indicates that actions are allowed to proceed, and a <code>CLOSED</code> calendar indicates that actions aren't allowed to proceed.</p>"""
    at_time: NotRequired["aws_sdk_ssm.types.iso8601_string.ISO8601String"]
    r"""<p>The time, as an <a href=\"https://en.wikipedia.org/wiki/ISO_8601\">ISO 8601</a> string, that you specified in your command. If you don't specify a time, <code>GetCalendarState</code> uses the current time.</p>"""
    next_transition_time: NotRequired["aws_sdk_ssm.types.iso8601_string.ISO8601String"]
    r"""<p>The time, as an <a href=\"https://en.wikipedia.org/wiki/ISO_8601\">ISO 8601</a> string, that the calendar state will change. If the current calendar state is <code>OPEN</code>, <code>NextTransitionTime</code> indicates when the calendar state changes to <code>CLOSED</code>, and vice-versa.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCalendarStateResponse) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_ssm.types.calendar_state

        out["State"] = aws_sdk_ssm.types.calendar_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "at_time" in value:
        out["AtTime"] = value["at_time"]
    if "next_transition_time" in value:
        out["NextTransitionTime"] = value["next_transition_time"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCalendarStateResponse:
    out: GetCalendarStateResponse = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_ssm.types.calendar_state

        out["state"] = aws_sdk_ssm.types.calendar_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "AtTime" in data:
        out["at_time"] = data["AtTime"]
    if "NextTransitionTime" in data:
        out["next_transition_time"] = data["NextTransitionTime"]
    return out
