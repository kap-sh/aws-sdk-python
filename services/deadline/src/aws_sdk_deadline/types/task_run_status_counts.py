"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunStatusCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.integer
    import aws_sdk_deadline.types.task_run_status

TaskRunStatusCounts: TypeAlias = dict[
    "aws_sdk_deadline.types.task_run_status.TaskRunStatus",
    "aws_sdk_deadline.types.integer.Integer",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TaskRunStatusCounts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_deadline.types.task_run_status

        out[aws_sdk_deadline.types.task_run_status.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> TaskRunStatusCounts:
    out: TaskRunStatusCounts = {}
    for key, value in data.items():
        import aws_sdk_deadline.types.task_run_status

        out[aws_sdk_deadline.types.task_run_status.deserialize_json(key)] = value
    return out
