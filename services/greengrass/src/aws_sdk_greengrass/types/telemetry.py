"""Generated from Smithy shape ``com.amazonaws.greengrass#Telemetry``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrass.errors import DeserializationError

Telemetry: TypeAlias = Literal[
    "On",
    "Off",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "On",
        "Off",
    )
)


def serialize_json(value: Telemetry) -> str:
    return value


def deserialize_json(data: str) -> Telemetry:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Telemetry value: {data!r}")
    return cast(Telemetry, data)
