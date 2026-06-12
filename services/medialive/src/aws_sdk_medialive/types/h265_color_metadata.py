"""Generated from Smithy shape ``com.amazonaws.medialive#H265ColorMetadata``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""H265 Color Metadata"""
H265ColorMetadata: TypeAlias = Literal[
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


def serialize_json(value: H265ColorMetadata) -> str:
    return value


def deserialize_json(data: str) -> H265ColorMetadata:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265ColorMetadata value: {data!r}")
    return cast(H265ColorMetadata, data)
