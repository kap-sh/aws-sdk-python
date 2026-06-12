"""Generated from Smithy shape ``com.amazonaws.ssm#AlarmList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.alarm

AlarmList: TypeAlias = list["aws_sdk_ssm.types.alarm.Alarm"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlarmList) -> list:
    import aws_sdk_ssm.types.alarm

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.alarm.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AlarmList:
    import aws_sdk_ssm.types.alarm

    out: AlarmList = []
    for item in data:
        out.append(aws_sdk_ssm.types.alarm.deserialize_aws_json_1_1(item))
    return out
