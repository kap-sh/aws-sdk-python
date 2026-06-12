"""Generated from Smithy shape ``com.amazonaws.iotevents#OnEnterLifecycle``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.events


class OnEnterLifecycle(TypedDict):
    events: NotRequired["aws_sdk_iot_events.types.events.Events"]
    """<p>Specifies the actions that are performed when the state is entered and the <code>condition</code> is <code>TRUE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnEnterLifecycle) -> dict:
    out: dict = {}
    if "events" in value:
        import aws_sdk_iot_events.types.events

        out["events"] = aws_sdk_iot_events.types.events.serialize_json(value["events"])
    return out


def deserialize_json(data: dict) -> OnEnterLifecycle:
    out: OnEnterLifecycle = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_iot_events.types.events

        out["events"] = aws_sdk_iot_events.types.events.deserialize_json(data["events"])
    return out
