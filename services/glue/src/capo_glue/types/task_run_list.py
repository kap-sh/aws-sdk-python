"""Generated from Smithy shape ``com.amazonaws.glue#TaskRunList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.task_run

TaskRunList: TypeAlias = list["capo_glue.types.task_run.TaskRun"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskRunList) -> list:
    import capo_glue.types.task_run

    out: list = []
    for item in value:
        out.append(capo_glue.types.task_run.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskRunList:
    import capo_glue.types.task_run

    out: TaskRunList = []
    for item in data:
        out.append(capo_glue.types.task_run.deserialize_aws_json_1_1(item))
    return out
