"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ConfigurationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

ConfigurationState: TypeAlias = Literal[
    "ACTIVE",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "UPDATE_IN_PROGRESS",
        "UPDATE_FAILED",
    )
)


def serialize_json(value: ConfigurationState) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationState value: {data!r}")
    return cast(ConfigurationState, data)
