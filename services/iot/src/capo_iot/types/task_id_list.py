"""Generated from Smithy shape ``com.amazonaws.iot#TaskIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.task_id

TaskIdList: TypeAlias = list["capo_iot.types.task_id.TaskId"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> TaskIdList:
    return list(data)
