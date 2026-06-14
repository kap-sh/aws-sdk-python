"""Generated from Smithy shape ``com.amazonaws.workspacesweb#FolderStructure``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_web.errors import DeserializationError

FolderStructure: TypeAlias = Literal[
    "Flat",
    "NestedByDate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Flat",
        "NestedByDate",
    )
)


def serialize_json(value: FolderStructure) -> str:
    return value


def deserialize_json(data: str) -> FolderStructure:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FolderStructure value: {data!r}")
    return cast(FolderStructure, data)
