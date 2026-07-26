"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunStatusCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.integer
    import capo_deadline.types.task_run_status

TaskRunStatusCounts: TypeAlias = dict[
    "capo_deadline.types.task_run_status.TaskRunStatus",
    "capo_deadline.types.integer.Integer",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TaskRunStatusCounts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_deadline.types.task_run_status

        out[capo_deadline.types.task_run_status.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> TaskRunStatusCounts:
    out: TaskRunStatusCounts = {}
    for key, value in data.items():
        import capo_deadline.types.task_run_status

        out[capo_deadline.types.task_run_status.deserialize_json(key)] = value
    return out
