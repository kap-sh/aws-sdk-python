"""Generated from Smithy shape ``com.amazonaws.medialive#H264LookAheadRateControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Look Ahead Rate Control"""
H264LookAheadRateControl: TypeAlias = Literal[
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


def serialize_json(value: H264LookAheadRateControl) -> str:
    return value


def deserialize_json(data: str) -> H264LookAheadRateControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264LookAheadRateControl value: {data!r}")
    return cast(H264LookAheadRateControl, data)
