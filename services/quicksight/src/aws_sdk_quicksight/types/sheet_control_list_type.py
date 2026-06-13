"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlListType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SheetControlListType: TypeAlias = Literal[
    "MULTI_SELECT",
    "SINGLE_SELECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MULTI_SELECT",
        "SINGLE_SELECT",
    )
)


def serialize_json(value: SheetControlListType) -> str:
    return value


def deserialize_json(data: str) -> SheetControlListType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SheetControlListType value: {data!r}")
    return cast(SheetControlListType, data)
