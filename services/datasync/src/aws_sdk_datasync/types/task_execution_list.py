"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datasync.types.task_execution_list_entry

TaskExecutionList: TypeAlias = list[
    "aws_sdk_datasync.types.task_execution_list_entry.TaskExecutionListEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskExecutionList) -> list:
    import aws_sdk_datasync.types.task_execution_list_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datasync.types.task_execution_list_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TaskExecutionList:
    import aws_sdk_datasync.types.task_execution_list_entry

    out: TaskExecutionList = []
    for item in data:
        out.append(
            aws_sdk_datasync.types.task_execution_list_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
