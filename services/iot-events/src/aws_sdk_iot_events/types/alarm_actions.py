"""Generated from Smithy shape ``com.amazonaws.iotevents#AlarmActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.alarm_action

AlarmActions: TypeAlias = list["aws_sdk_iot_events.types.alarm_action.AlarmAction"]


# --- restJson1 ser/de ---
def serialize_json(value: AlarmActions) -> list:
    import aws_sdk_iot_events.types.alarm_action

    out: list = []
    for item in value:
        out.append(aws_sdk_iot_events.types.alarm_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> AlarmActions:
    import aws_sdk_iot_events.types.alarm_action

    out: AlarmActions = []
    for item in data:
        out.append(aws_sdk_iot_events.types.alarm_action.deserialize_json(item))
    return out
