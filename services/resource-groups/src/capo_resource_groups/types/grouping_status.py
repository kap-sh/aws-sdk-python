"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupingStatus``."""

from typing import Literal, TypeAlias, cast

GroupingStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILED",
    "IN_PROGRESS",
    "SKIPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingStatus) -> str:
    return value


def deserialize_json(data: str) -> GroupingStatus:
    return cast(GroupingStatus, data)
