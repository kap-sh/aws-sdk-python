"""Generated from Smithy shape ``com.amazonaws.fsx#TaskIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.task_id

TaskIds: TypeAlias = list["aws_sdk_fsx.types.task_id.TaskId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TaskIds:
    return list(data)
