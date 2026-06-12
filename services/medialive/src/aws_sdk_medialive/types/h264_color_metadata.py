"""Generated from Smithy shape ``com.amazonaws.medialive#H264ColorMetadata``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H264 Color Metadata"""
H264ColorMetadata: TypeAlias = Literal[
    "IGNORE",
    "INSERT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IGNORE",
        "INSERT",
    )
)


def serialize_json(value: H264ColorMetadata) -> str:
    return value


def deserialize_json(data: str) -> H264ColorMetadata:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H264ColorMetadata value: {data!r}")
    return cast(H264ColorMetadata, data)
