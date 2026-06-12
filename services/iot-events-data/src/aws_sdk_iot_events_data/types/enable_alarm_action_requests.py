"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#EnableAlarmActionRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.enable_alarm_action_request

EnableAlarmActionRequests: TypeAlias = list[
    "aws_sdk_iot_events_data.types.enable_alarm_action_request.EnableAlarmActionRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnableAlarmActionRequests) -> list:
    import aws_sdk_iot_events_data.types.enable_alarm_action_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_events_data.types.enable_alarm_action_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EnableAlarmActionRequests:
    import aws_sdk_iot_events_data.types.enable_alarm_action_request

    out: EnableAlarmActionRequests = []
    for item in data:
        out.append(
            aws_sdk_iot_events_data.types.enable_alarm_action_request.deserialize_json(
                item
            )
        )
    return out
