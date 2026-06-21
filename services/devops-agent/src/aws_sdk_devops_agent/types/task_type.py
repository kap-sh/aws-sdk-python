"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskType``."""

from typing import Literal, TypeAlias, cast

"""<p>Types of tasks that can be created in the backlog</p>"""
TaskType: TypeAlias = Literal[
    "INVESTIGATION",
    "EVALUATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskType) -> str:
    return value


def deserialize_json(data: str) -> TaskType:
    return cast(TaskType, data)
