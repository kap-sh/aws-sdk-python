"""Generated from Smithy shape ``com.amazonaws.lightsail#NotificationTriggerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.alarm_state

NotificationTriggerList: TypeAlias = list[
    "aws_sdk_lightsail.types.alarm_state.AlarmState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationTriggerList) -> list:
    import aws_sdk_lightsail.types.alarm_state

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.alarm_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NotificationTriggerList:
    import aws_sdk_lightsail.types.alarm_state

    out: NotificationTriggerList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.alarm_state.deserialize_aws_json_1_1(item))
    return out
