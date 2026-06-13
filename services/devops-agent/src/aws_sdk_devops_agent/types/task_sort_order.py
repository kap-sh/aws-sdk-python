"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Sort order options</p>"""
TaskSortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_json(value: TaskSortOrder) -> str:
    return value


def deserialize_json(data: str) -> TaskSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskSortOrder value: {data!r}")
    return cast(TaskSortOrder, data)
