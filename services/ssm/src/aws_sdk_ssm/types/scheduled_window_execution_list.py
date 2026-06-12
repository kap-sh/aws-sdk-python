"""Generated from Smithy shape ``com.amazonaws.ssm#ScheduledWindowExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.scheduled_window_execution

ScheduledWindowExecutionList: TypeAlias = list[
    "aws_sdk_ssm.types.scheduled_window_execution.ScheduledWindowExecution"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduledWindowExecutionList) -> list:
    import aws_sdk_ssm.types.scheduled_window_execution

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.scheduled_window_execution.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScheduledWindowExecutionList:
    import aws_sdk_ssm.types.scheduled_window_execution

    out: ScheduledWindowExecutionList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.scheduled_window_execution.deserialize_aws_json_1_1(item)
        )
    return out
