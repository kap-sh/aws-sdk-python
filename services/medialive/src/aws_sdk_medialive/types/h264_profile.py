"""Generated from Smithy shape ``com.amazonaws.medialive#H264Profile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Profile"""
H264Profile: TypeAlias = Literal[
    "BASELINE",
    "HIGH",
    "HIGH_10BIT",
    "HIGH_422",
    "HIGH_422_10BIT",
    "MAIN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASELINE",
        "HIGH",
        "HIGH_10BIT",
        "HIGH_422",
        "HIGH_422_10BIT",
        "MAIN",
    )
)


def serialize_json(value: H264Profile) -> str:
    return value


def deserialize_json(data: str) -> H264Profile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264Profile value: {data!r}")
    return cast(H264Profile, data)
