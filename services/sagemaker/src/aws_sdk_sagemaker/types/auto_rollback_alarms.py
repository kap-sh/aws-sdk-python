"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoRollbackAlarms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.alarm_details

AutoRollbackAlarms: TypeAlias = list[
    "aws_sdk_sagemaker.types.alarm_details.AlarmDetails"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoRollbackAlarms) -> list:
    import aws_sdk_sagemaker.types.alarm_details

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.alarm_details.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AutoRollbackAlarms:
    import aws_sdk_sagemaker.types.alarm_details

    out: AutoRollbackAlarms = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.alarm_details.deserialize_aws_json_1_1(item))
    return out
