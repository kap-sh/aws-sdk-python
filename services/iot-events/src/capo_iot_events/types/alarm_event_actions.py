"""Generated from Smithy shape ``com.amazonaws.iotevents#AlarmEventActions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.alarm_actions


class AlarmEventActions(TypedDict, closed=True):
    alarm_actions: NotRequired["capo_iot_events.types.alarm_actions.AlarmActions"]
    """<p>Specifies one or more supported actions to receive notifications when the alarm state changes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AlarmEventActions) -> dict:
    out: dict = {}
    if "alarm_actions" in value:
        import capo_iot_events.types.alarm_actions

        out["alarmActions"] = capo_iot_events.types.alarm_actions.serialize_json(
            value["alarm_actions"]
        )
    return out


def deserialize_json(data: dict) -> AlarmEventActions:
    out: AlarmEventActions = {}  # type: ignore[typeddict-item]
    if "alarmActions" in data:
        import capo_iot_events.types.alarm_actions

        out["alarm_actions"] = capo_iot_events.types.alarm_actions.deserialize_json(
            data["alarmActions"]
        )
    return out
