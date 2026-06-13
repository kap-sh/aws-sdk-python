"""Generated from Smithy shape ``com.amazonaws.quicksight#IncludeFolderMembers``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

IncludeFolderMembers: TypeAlias = Literal[
    "RECURSE",
    "ONE_LEVEL",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RECURSE",
        "ONE_LEVEL",
        "NONE",
    )
)


def serialize_json(value: IncludeFolderMembers) -> str:
    return value


def deserialize_json(data: str) -> IncludeFolderMembers:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IncludeFolderMembers value: {data!r}")
    return cast(IncludeFolderMembers, data)
