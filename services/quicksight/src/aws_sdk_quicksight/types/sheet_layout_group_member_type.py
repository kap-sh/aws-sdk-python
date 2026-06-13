"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetLayoutGroupMemberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SheetLayoutGroupMemberType: TypeAlias = Literal[
    "ELEMENT",
    "GROUP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ELEMENT",
        "GROUP",
    )
)


def serialize_json(value: SheetLayoutGroupMemberType) -> str:
    return value


def deserialize_json(data: str) -> SheetLayoutGroupMemberType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SheetLayoutGroupMemberType value: {data!r}"
        )
    return cast(SheetLayoutGroupMemberType, data)
