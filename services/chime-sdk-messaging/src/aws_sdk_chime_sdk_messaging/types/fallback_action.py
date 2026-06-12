"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#FallbackAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

FallbackAction: TypeAlias = Literal[
    "CONTINUE",
    "ABORT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTINUE",
        "ABORT",
    )
)


def serialize_json(value: FallbackAction) -> str:
    return value


def deserialize_json(data: str) -> FallbackAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FallbackAction value: {data!r}")
    return cast(FallbackAction, data)
