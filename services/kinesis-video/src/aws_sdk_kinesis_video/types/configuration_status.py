"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

ConfigurationStatus: TypeAlias = Literal[
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


def serialize_json(value: ConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationStatus value: {data!r}")
    return cast(ConfigurationStatus, data)
