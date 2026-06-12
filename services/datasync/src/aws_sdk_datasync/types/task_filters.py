"""Generated from Smithy shape ``com.amazonaws.datasync#TaskFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datasync.types.task_filter

TaskFilters: TypeAlias = list["aws_sdk_datasync.types.task_filter.TaskFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskFilters) -> list:
    import aws_sdk_datasync.types.task_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_datasync.types.task_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskFilters:
    import aws_sdk_datasync.types.task_filter

    out: TaskFilters = []
    for item in data:
        out.append(aws_sdk_datasync.types.task_filter.deserialize_aws_json_1_1(item))
    return out
