"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#EventInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.event_name
    import aws_sdk_codeguru_reviewer.types.event_state


class EventInfo(TypedDict):
    name: NotRequired["aws_sdk_codeguru_reviewer.types.event_name.EventName"]
    """<p>The name of the event. The possible names are <code>pull_request</code>, <code>workflow_dispatch</code>, <code>schedule</code>, and <code>push</code> </p>"""
    state: NotRequired["aws_sdk_codeguru_reviewer.types.event_state.EventState"]
    """<p>The state of an event. The state might be open, closed, or another state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "state" in value:
        out["State"] = value["state"]
    return out


def deserialize_json(data: dict) -> EventInfo:
    out: EventInfo = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "State" in data:
        out["state"] = data["State"]
    return out
