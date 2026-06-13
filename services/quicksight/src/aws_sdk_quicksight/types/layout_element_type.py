"""Generated from Smithy shape ``com.amazonaws.quicksight#LayoutElementType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

LayoutElementType: TypeAlias = Literal[
    "VISUAL",
    "FILTER_CONTROL",
    "PARAMETER_CONTROL",
    "TEXT_BOX",
    "IMAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VISUAL",
        "FILTER_CONTROL",
        "PARAMETER_CONTROL",
        "TEXT_BOX",
        "IMAGE",
    )
)


def serialize_json(value: LayoutElementType) -> str:
    return value


def deserialize_json(data: str) -> LayoutElementType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LayoutElementType value: {data!r}")
    return cast(LayoutElementType, data)
