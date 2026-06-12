"""Generated from Smithy shape ``com.amazonaws.medialive#H264QualityLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Quality Level"""
H264QualityLevel: TypeAlias = Literal[
    "ENHANCED_QUALITY",
    "STANDARD_QUALITY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENHANCED_QUALITY",
        "STANDARD_QUALITY",
    )
)


def serialize_json(value: H264QualityLevel) -> str:
    return value


def deserialize_json(data: str) -> H264QualityLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264QualityLevel value: {data!r}")
    return cast(H264QualityLevel, data)
