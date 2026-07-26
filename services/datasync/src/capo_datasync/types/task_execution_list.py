"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.task_execution_list_entry

TaskExecutionList: TypeAlias = list[
    "capo_datasync.types.task_execution_list_entry.TaskExecutionListEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskExecutionList) -> list:
    import capo_datasync.types.task_execution_list_entry

    out: list = []
    for item in value:
        out.append(
            capo_datasync.types.task_execution_list_entry.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TaskExecutionList:
    import capo_datasync.types.task_execution_list_entry

    out: TaskExecutionList = []
    for item in data:
        out.append(
            capo_datasync.types.task_execution_list_entry.deserialize_aws_json_1_1(item)
        )
    return out
