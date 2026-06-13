"""Generated from Smithy shape ``com.amazonaws.groundstation#FrequencyUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

FrequencyUnits: TypeAlias = Literal[
    "GHz",
    "MHz",
    "kHz",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GHz",
        "MHz",
        "kHz",
    )
)


def serialize_json(value: FrequencyUnits) -> str:
    return value


def deserialize_json(data: str) -> FrequencyUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FrequencyUnits value: {data!r}")
    return cast(FrequencyUnits, data)
