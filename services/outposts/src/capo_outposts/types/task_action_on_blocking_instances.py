"""Generated from Smithy shape ``com.amazonaws.outposts#TaskActionOnBlockingInstances``."""

from typing import Literal, TypeAlias, cast

TaskActionOnBlockingInstances: TypeAlias = Literal[
    "WAIT_FOR_EVACUATION",
    "FAIL_TASK",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskActionOnBlockingInstances) -> str:
    return value


def deserialize_json(data: str) -> TaskActionOnBlockingInstances:
    return cast(TaskActionOnBlockingInstances, data)
