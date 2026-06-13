"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskSortField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Fields available for sorting tasks</p>"""
TaskSortField: TypeAlias = Literal[
    "CREATED_AT",
    "PRIORITY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED_AT",
        "PRIORITY",
    )
)


def serialize_json(value: TaskSortField) -> str:
    return value


def deserialize_json(data: str) -> TaskSortField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskSortField value: {data!r}")
    return cast(TaskSortField, data)
