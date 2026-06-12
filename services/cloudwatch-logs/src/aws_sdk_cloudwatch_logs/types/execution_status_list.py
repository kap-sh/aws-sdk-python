"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ExecutionStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.execution_status

ExecutionStatusList: TypeAlias = list[
    "aws_sdk_cloudwatch_logs.types.execution_status.ExecutionStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionStatusList) -> list:
    import aws_sdk_cloudwatch_logs.types.execution_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch_logs.types.execution_status.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExecutionStatusList:
    import aws_sdk_cloudwatch_logs.types.execution_status

    out: ExecutionStatusList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch_logs.types.execution_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
