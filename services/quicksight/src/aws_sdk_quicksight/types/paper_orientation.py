"""Generated from Smithy shape ``com.amazonaws.quicksight#PaperOrientation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

PaperOrientation: TypeAlias = Literal[
    "PORTRAIT",
    "LANDSCAPE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PORTRAIT",
        "LANDSCAPE",
    )
)


def serialize_json(value: PaperOrientation) -> str:
    return value


def deserialize_json(data: str) -> PaperOrientation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaperOrientation value: {data!r}")
    return cast(PaperOrientation, data)
