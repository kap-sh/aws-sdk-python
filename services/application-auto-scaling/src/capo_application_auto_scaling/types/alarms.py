"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#Alarms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_auto_scaling.types.alarm

Alarms: TypeAlias = list["capo_application_auto_scaling.types.alarm.Alarm"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Alarms) -> list:
    import capo_application_auto_scaling.types.alarm

    out: list = []
    for item in value:
        out.append(
            capo_application_auto_scaling.types.alarm.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Alarms:
    import capo_application_auto_scaling.types.alarm

    out: Alarms = []
    for item in data:
        out.append(
            capo_application_auto_scaling.types.alarm.deserialize_aws_json_1_1(item)
        )
    return out
