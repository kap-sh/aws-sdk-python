"""Generated from Smithy shape ``com.amazonaws.datasync#TaskList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.task_list_entry

TaskList: TypeAlias = list["capo_datasync.types.task_list_entry.TaskListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskList) -> list:
    import capo_datasync.types.task_list_entry

    out: list = []
    for item in value:
        out.append(capo_datasync.types.task_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskList:
    import capo_datasync.types.task_list_entry

    out: TaskList = []
    for item in data:
        out.append(capo_datasync.types.task_list_entry.deserialize_aws_json_1_1(item))
    return out
