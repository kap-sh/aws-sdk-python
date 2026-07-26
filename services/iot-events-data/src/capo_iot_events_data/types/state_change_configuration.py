"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#StateChangeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.trigger_type


class StateChangeConfiguration(TypedDict, closed=True):
    trigger_type: NotRequired["capo_iot_events_data.types.trigger_type.TriggerType"]
    """<p>The trigger type. If the value is <code>SNOOZE_TIMEOUT</code>, the snooze duration ends and the alarm automatically changes to the <code>NORMAL</code> state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StateChangeConfiguration) -> dict:
    out: dict = {}
    if "trigger_type" in value:
        import capo_iot_events_data.types.trigger_type

        out["triggerType"] = capo_iot_events_data.types.trigger_type.serialize_json(
            value["trigger_type"]
        )
    return out


def deserialize_json(data: dict) -> StateChangeConfiguration:
    out: StateChangeConfiguration = {}  # type: ignore[typeddict-item]
    if "triggerType" in data:
        import capo_iot_events_data.types.trigger_type

        out["trigger_type"] = capo_iot_events_data.types.trigger_type.deserialize_json(
            data["triggerType"]
        )
    return out
