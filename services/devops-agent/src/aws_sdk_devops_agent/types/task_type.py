"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Types of tasks that can be created in the backlog</p>"""
TaskType: TypeAlias = Literal[
    "INVESTIGATION",
    "EVALUATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVESTIGATION",
        "EVALUATION",
    )
)


def serialize_json(value: TaskType) -> str:
    return value


def deserialize_json(data: str) -> TaskType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskType value: {data!r}")
    return cast(TaskType, data)
