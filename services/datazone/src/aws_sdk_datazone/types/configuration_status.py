"""Generated from Smithy shape ``com.amazonaws.datazone#ConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

ConfigurationStatus: TypeAlias = Literal[
    "COMPLETED",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "FAILED",
    )
)


def serialize_json(value: ConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationStatus value: {data!r}")
    return cast(ConfigurationStatus, data)
