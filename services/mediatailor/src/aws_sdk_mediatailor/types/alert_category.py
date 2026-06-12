"""Generated from Smithy shape ``com.amazonaws.mediatailor#AlertCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

AlertCategory: TypeAlias = Literal[
    "SCHEDULING_ERROR",
    "PLAYBACK_WARNING",
    "INFO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULING_ERROR",
        "PLAYBACK_WARNING",
        "INFO",
    )
)


def serialize_json(value: AlertCategory) -> str:
    return value


def deserialize_json(data: str) -> AlertCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlertCategory value: {data!r}")
    return cast(AlertCategory, data)
