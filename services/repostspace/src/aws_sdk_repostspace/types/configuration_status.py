"""Generated from Smithy shape ``com.amazonaws.repostspace#ConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_repostspace.errors import DeserializationError

ConfigurationStatus: TypeAlias = Literal[
    "CONFIGURED",
    "UNCONFIGURED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONFIGURED",
        "UNCONFIGURED",
    )
)


def serialize_json(value: ConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationStatus value: {data!r}")
    return cast(ConfigurationStatus, data)
