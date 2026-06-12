"""Generated from Smithy shape ``com.amazonaws.medialive#H265LookAheadRateControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Look Ahead Rate Control"""
H265LookAheadRateControl: TypeAlias = Literal[
    "HIGH",
    "LOW",
    "MEDIUM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HIGH",
        "LOW",
        "MEDIUM",
    )
)


def serialize_json(value: H265LookAheadRateControl) -> str:
    return value


def deserialize_json(data: str) -> H265LookAheadRateControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265LookAheadRateControl value: {data!r}")
    return cast(H265LookAheadRateControl, data)
