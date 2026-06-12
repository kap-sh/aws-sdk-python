"""Generated from Smithy shape ``com.amazonaws.pinpoint#ButtonAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

ButtonAction: TypeAlias = Literal[
    "LINK",
    "DEEP_LINK",
    "CLOSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINK",
        "DEEP_LINK",
        "CLOSE",
    )
)


def serialize_json(value: ButtonAction) -> str:
    return value


def deserialize_json(data: str) -> ButtonAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ButtonAction value: {data!r}")
    return cast(ButtonAction, data)
