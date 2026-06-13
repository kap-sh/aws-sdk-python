"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

SheetContentType: TypeAlias = Literal[
    "PAGINATED",
    "INTERACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PAGINATED",
        "INTERACTIVE",
    )
)


def serialize_json(value: SheetContentType) -> str:
    return value


def deserialize_json(data: str) -> SheetContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SheetContentType value: {data!r}")
    return cast(SheetContentType, data)
