"""Generated from Smithy shape ``com.amazonaws.lightsail#AlarmsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.alarm

AlarmsList: TypeAlias = list["capo_lightsail.types.alarm.Alarm"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlarmsList) -> list:
    import capo_lightsail.types.alarm

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.alarm.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AlarmsList:
    import capo_lightsail.types.alarm

    out: AlarmsList = []
    for item in data:
        out.append(capo_lightsail.types.alarm.deserialize_aws_json_1_1(item))
    return out
