"""Generated from Smithy shape ``com.amazonaws.ivs#TranscodePreset``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs.errors import DeserializationError

TranscodePreset: TypeAlias = Literal[
    "HIGHER_BANDWIDTH_DELIVERY",
    "CONSTRAINED_BANDWIDTH_DELIVERY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIGHER_BANDWIDTH_DELIVERY",
        "CONSTRAINED_BANDWIDTH_DELIVERY",
    )
)


def serialize_json(value: TranscodePreset) -> str:
    return value


def deserialize_json(data: str) -> TranscodePreset:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TranscodePreset value: {data!r}")
    return cast(TranscodePreset, data)
