"""Generated from Smithy shape ``com.amazonaws.glue#TaskRunList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.task_run

TaskRunList: TypeAlias = list["aws_sdk_glue.types.task_run.TaskRun"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskRunList) -> list:
    import aws_sdk_glue.types.task_run

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.task_run.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskRunList:
    import aws_sdk_glue.types.task_run

    out: TaskRunList = []
    for item in data:
        out.append(aws_sdk_glue.types.task_run.deserialize_aws_json_1_1(item))
    return out
