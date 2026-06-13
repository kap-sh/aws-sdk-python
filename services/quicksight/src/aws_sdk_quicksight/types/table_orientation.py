"""Generated from Smithy shape ``com.amazonaws.quicksight#TableOrientation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

TableOrientation: TypeAlias = Literal[
    "VERTICAL",
    "HORIZONTAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VERTICAL",
        "HORIZONTAL",
    )
)


def serialize_json(value: TableOrientation) -> str:
    return value


def deserialize_json(data: str) -> TableOrientation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableOrientation value: {data!r}")
    return cast(TableOrientation, data)
