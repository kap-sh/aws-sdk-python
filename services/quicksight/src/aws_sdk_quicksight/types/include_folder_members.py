"""Generated from Smithy shape ``com.amazonaws.quicksight#IncludeFolderMembers``."""

from typing import Literal, TypeAlias, cast

IncludeFolderMembers: TypeAlias = Literal[
    "RECURSE",
    "ONE_LEVEL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludeFolderMembers) -> str:
    return value


def deserialize_json(data: str) -> IncludeFolderMembers:
    return cast(IncludeFolderMembers, data)
