"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupingType``."""

from typing import Literal, TypeAlias, cast

GroupingType: TypeAlias = Literal[
    "GROUP",
    "UNGROUP",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingType) -> str:
    return value


def deserialize_json(data: str) -> GroupingType:
    return cast(GroupingType, data)
