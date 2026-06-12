"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#AcknowledgeAlarmActionRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.acknowledge_alarm_action_request

AcknowledgeAlarmActionRequests: TypeAlias = list[
    "aws_sdk_iot_events_data.types.acknowledge_alarm_action_request.AcknowledgeAlarmActionRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: AcknowledgeAlarmActionRequests) -> list:
    import aws_sdk_iot_events_data.types.acknowledge_alarm_action_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_events_data.types.acknowledge_alarm_action_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AcknowledgeAlarmActionRequests:
    import aws_sdk_iot_events_data.types.acknowledge_alarm_action_request

    out: AcknowledgeAlarmActionRequests = []
    for item in data:
        out.append(
            aws_sdk_iot_events_data.types.acknowledge_alarm_action_request.deserialize_json(
                item
            )
        )
    return out
