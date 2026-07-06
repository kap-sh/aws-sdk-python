"""Generated from Smithy shape ``com.amazonaws.iotevents#OnExitLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.events


class OnExitLifecycle(TypedDict, closed=True):
    events: NotRequired["aws_sdk_iot_events.types.events.Events"]
    """<p>Specifies the <code>actions</code> that are performed when the state is exited and the <code>condition</code> is <code>TRUE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnExitLifecycle) -> dict:
    out: dict = {}
    if "events" in value:
        import aws_sdk_iot_events.types.events

        out["events"] = aws_sdk_iot_events.types.events.serialize_json(value["events"])
    return out


def deserialize_json(data: dict) -> OnExitLifecycle:
    out: OnExitLifecycle = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import aws_sdk_iot_events.types.events

        out["events"] = aws_sdk_iot_events.types.events.deserialize_json(data["events"])
    return out
