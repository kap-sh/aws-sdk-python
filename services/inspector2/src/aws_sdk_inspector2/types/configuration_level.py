"""Generated from Smithy shape ``com.amazonaws.inspector2#ConfigurationLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

ConfigurationLevel: TypeAlias = Literal[
    "ORGANIZATION",
    "ACCOUNT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ORGANIZATION",
        "ACCOUNT",
    )
)


def serialize_json(value: ConfigurationLevel) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationLevel value: {data!r}")
    return cast(ConfigurationLevel, data)
