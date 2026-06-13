"""Generated from Smithy shape ``com.amazonaws.qbusiness#PluginState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

PluginState: TypeAlias = Literal[
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


def serialize_json(value: PluginState) -> str:
    return value


def deserialize_json(data: str) -> PluginState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PluginState value: {data!r}")
    return cast(PluginState, data)
