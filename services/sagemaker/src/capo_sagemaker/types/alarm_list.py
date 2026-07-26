"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlarmList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.alarm

AlarmList: TypeAlias = list["capo_sagemaker.types.alarm.Alarm"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlarmList) -> list:
    import capo_sagemaker.types.alarm

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.alarm.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AlarmList:
    import capo_sagemaker.types.alarm

    out: AlarmList = []
    for item in data:
        out.append(capo_sagemaker.types.alarm.deserialize_aws_json_1_1(item))
    return out
