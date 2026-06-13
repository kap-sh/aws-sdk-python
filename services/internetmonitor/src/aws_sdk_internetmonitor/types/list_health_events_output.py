"""Generated from Smithy shape ``com.amazonaws.internetmonitor#ListHealthEventsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.health_event_list


class ListHealthEventsOutput(TypedDict):
    health_events: "aws_sdk_internetmonitor.types.health_event_list.HealthEventList"
    """<p>A list of health events.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListHealthEventsOutput) -> dict:
    out: dict = {}
    import aws_sdk_internetmonitor.types.health_event_list

    out["HealthEvents"] = (
        aws_sdk_internetmonitor.types.health_event_list.serialize_json(
            value["health_events"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListHealthEventsOutput:
    out: ListHealthEventsOutput = {}  # type: ignore[typeddict-item]
    if "HealthEvents" in data:
        import aws_sdk_internetmonitor.types.health_event_list

        out["health_events"] = (
            aws_sdk_internetmonitor.types.health_event_list.deserialize_json(
                data["HealthEvents"]
            )
        )
    else:
        raise DeserializationError("ListHealthEventsOutput.health_events required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
