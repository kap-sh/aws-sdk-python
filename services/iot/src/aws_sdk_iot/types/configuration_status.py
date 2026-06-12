"""Generated from Smithy shape ``com.amazonaws.iot#ConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ConfigurationStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
    )
)


def serialize_json(value: ConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationStatus value: {data!r}")
    return cast(ConfigurationStatus, data)
