"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AutoRefreshMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

AutoRefreshMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: AutoRefreshMode) -> str:
    return value


def deserialize_json(data: str) -> AutoRefreshMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoRefreshMode value: {data!r}")
    return cast(AutoRefreshMode, data)
