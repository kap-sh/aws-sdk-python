"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#ResetAlarmActionRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.reset_alarm_action_request

ResetAlarmActionRequests: TypeAlias = list[
    "aws_sdk_iot_events_data.types.reset_alarm_action_request.ResetAlarmActionRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResetAlarmActionRequests) -> list:
    import aws_sdk_iot_events_data.types.reset_alarm_action_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_events_data.types.reset_alarm_action_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResetAlarmActionRequests:
    import aws_sdk_iot_events_data.types.reset_alarm_action_request

    out: ResetAlarmActionRequests = []
    for item in data:
        out.append(
            aws_sdk_iot_events_data.types.reset_alarm_action_request.deserialize_json(
                item
            )
        )
    return out
