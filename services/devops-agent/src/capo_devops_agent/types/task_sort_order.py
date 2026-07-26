"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskSortOrder``."""

from typing import Literal, TypeAlias, cast

"""<p>Sort order options</p>"""
TaskSortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskSortOrder) -> str:
    return value


def deserialize_json(data: str) -> TaskSortOrder:
    return cast(TaskSortOrder, data)
