"""Generated from Smithy shape ``com.amazonaws.datazone#EnableSetting``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

EnableSetting: TypeAlias = Literal[
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


def serialize_json(value: EnableSetting) -> str:
    return value


def deserialize_json(data: str) -> EnableSetting:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnableSetting value: {data!r}")
    return cast(EnableSetting, data)
