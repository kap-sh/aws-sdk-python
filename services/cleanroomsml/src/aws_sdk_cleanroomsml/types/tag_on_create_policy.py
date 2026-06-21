"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TagOnCreatePolicy``."""

from typing import Literal, TypeAlias, cast

TagOnCreatePolicy: TypeAlias = Literal[
    "FROM_PARENT_RESOURCE",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TagOnCreatePolicy) -> str:
    return value


def deserialize_json(data: str) -> TagOnCreatePolicy:
    return cast(TagOnCreatePolicy, data)
