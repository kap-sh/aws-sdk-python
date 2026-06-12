"""Generated from Smithy shape ``com.amazonaws.datasync#TaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datasync.types.task_list_entry

TaskList: TypeAlias = list["aws_sdk_datasync.types.task_list_entry.TaskListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskList) -> list:
    import aws_sdk_datasync.types.task_list_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_datasync.types.task_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskList:
    import aws_sdk_datasync.types.task_list_entry

    out: TaskList = []
    for item in data:
        out.append(
            aws_sdk_datasync.types.task_list_entry.deserialize_aws_json_1_1(item)
        )
    return out
