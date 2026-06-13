"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

CustomContentType: TypeAlias = Literal[
    "IMAGE",
    "OTHER_EMBEDDED_CONTENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMAGE",
        "OTHER_EMBEDDED_CONTENT",
    )
)


def serialize_json(value: CustomContentType) -> str:
    return value


def deserialize_json(data: str) -> CustomContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomContentType value: {data!r}")
    return cast(CustomContentType, data)
