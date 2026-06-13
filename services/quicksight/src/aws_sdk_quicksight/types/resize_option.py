"""Generated from Smithy shape ``com.amazonaws.quicksight#ResizeOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ResizeOption: TypeAlias = Literal[
    "FIXED",
    "RESPONSIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIXED",
        "RESPONSIVE",
    )
)


def serialize_json(value: ResizeOption) -> str:
    return value


def deserialize_json(data: str) -> ResizeOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResizeOption value: {data!r}")
    return cast(ResizeOption, data)
