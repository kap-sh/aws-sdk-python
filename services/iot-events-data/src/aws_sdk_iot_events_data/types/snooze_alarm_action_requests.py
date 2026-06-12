"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#SnoozeAlarmActionRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.snooze_alarm_action_request

SnoozeAlarmActionRequests: TypeAlias = list[
    "aws_sdk_iot_events_data.types.snooze_alarm_action_request.SnoozeAlarmActionRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnoozeAlarmActionRequests) -> list:
    import aws_sdk_iot_events_data.types.snooze_alarm_action_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_events_data.types.snooze_alarm_action_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SnoozeAlarmActionRequests:
    import aws_sdk_iot_events_data.types.snooze_alarm_action_request

    out: SnoozeAlarmActionRequests = []
    for item in data:
        out.append(
            aws_sdk_iot_events_data.types.snooze_alarm_action_request.deserialize_json(
                item
            )
        )
    return out
