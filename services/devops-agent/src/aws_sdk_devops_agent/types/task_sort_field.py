"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskSortField``."""

from typing import Literal, TypeAlias, cast

"""<p>Fields available for sorting tasks</p>"""
TaskSortField: TypeAlias = Literal[
    "CREATED_AT",
    "PRIORITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskSortField) -> str:
    return value


def deserialize_json(data: str) -> TaskSortField:
    return cast(TaskSortField, data)
