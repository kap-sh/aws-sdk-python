"""Generated from Smithy shape ``com.amazonaws.workspacesweb#FolderStructure``."""

from typing import Literal, TypeAlias, cast

FolderStructure: TypeAlias = Literal[
    "Flat",
    "NestedByDate",
]


# --- restJson1 ser/de ---
def serialize_json(value: FolderStructure) -> str:
    return value


def deserialize_json(data: str) -> FolderStructure:
    return cast(FolderStructure, data)
