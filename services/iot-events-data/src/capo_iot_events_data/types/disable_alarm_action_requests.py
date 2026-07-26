"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DisableAlarmActionRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events_data.types.disable_alarm_action_request

DisableAlarmActionRequests: TypeAlias = list[
    "capo_iot_events_data.types.disable_alarm_action_request.DisableAlarmActionRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: DisableAlarmActionRequests) -> list:
    import capo_iot_events_data.types.disable_alarm_action_request

    out: list = []
    for item in value:
        out.append(
            capo_iot_events_data.types.disable_alarm_action_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DisableAlarmActionRequests:
    import capo_iot_events_data.types.disable_alarm_action_request

    out: DisableAlarmActionRequests = []
    for item in data:
        out.append(
            capo_iot_events_data.types.disable_alarm_action_request.deserialize_json(
                item
            )
        )
    return out
