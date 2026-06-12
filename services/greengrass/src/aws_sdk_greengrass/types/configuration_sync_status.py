"""Generated from Smithy shape ``com.amazonaws.greengrass#ConfigurationSyncStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

ConfigurationSyncStatus: TypeAlias = Literal[
    "InSync",
    "OutOfSync",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InSync",
        "OutOfSync",
    )
)


def serialize_json(value: ConfigurationSyncStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationSyncStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationSyncStatus value: {data!r}")
    return cast(ConfigurationSyncStatus, data)
