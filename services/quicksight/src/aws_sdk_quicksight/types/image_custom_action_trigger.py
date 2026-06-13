"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageCustomActionTrigger``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ImageCustomActionTrigger: TypeAlias = Literal[
    "CLICK",
    "MENU",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLICK",
        "MENU",
    )
)


def serialize_json(value: ImageCustomActionTrigger) -> str:
    return value


def deserialize_json(data: str) -> ImageCustomActionTrigger:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImageCustomActionTrigger value: {data!r}")
    return cast(ImageCustomActionTrigger, data)
