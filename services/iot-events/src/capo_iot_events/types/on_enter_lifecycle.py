"""Generated from Smithy shape ``com.amazonaws.iotevents#OnEnterLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.events


class OnEnterLifecycle(TypedDict, closed=True):
    events: NotRequired["capo_iot_events.types.events.Events"]
    """<p>Specifies the actions that are performed when the state is entered and the <code>condition</code> is <code>TRUE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnEnterLifecycle) -> dict:
    out: dict = {}
    if "events" in value:
        import capo_iot_events.types.events

        out["events"] = capo_iot_events.types.events.serialize_json(value["events"])
    return out


def deserialize_json(data: dict) -> OnEnterLifecycle:
    out: OnEnterLifecycle = {}  # type: ignore[typeddict-item]
    if "events" in data:
        import capo_iot_events.types.events

        out["events"] = capo_iot_events.types.events.deserialize_json(data["events"])
    return out
