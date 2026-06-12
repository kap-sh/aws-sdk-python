"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConfigurationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

ConfigurationState: TypeAlias = Literal[
    "ENABLED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
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
