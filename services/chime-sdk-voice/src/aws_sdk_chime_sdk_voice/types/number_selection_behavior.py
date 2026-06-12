"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#NumberSelectionBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

NumberSelectionBehavior: TypeAlias = Literal[
    "PreferSticky",
    "AvoidSticky",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PreferSticky",
        "AvoidSticky",
    )
)


def serialize_json(value: NumberSelectionBehavior) -> str:
    return value


def deserialize_json(data: str) -> NumberSelectionBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NumberSelectionBehavior value: {data!r}")
    return cast(NumberSelectionBehavior, data)
