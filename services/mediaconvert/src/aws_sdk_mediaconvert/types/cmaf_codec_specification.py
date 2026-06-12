"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmafCodecSpecification``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specification to use (RFC-6381 or the default RFC-4281) during m3u8 playlist generation."""
CmafCodecSpecification: TypeAlias = Literal[
    "RFC_6381",
    "RFC_4281",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RFC_6381",
        "RFC_4281",
    )
)


def serialize_json(value: CmafCodecSpecification) -> str:
    return value


def deserialize_json(data: str) -> CmafCodecSpecification:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmafCodecSpecification value: {data!r}")
    return cast(CmafCodecSpecification, data)
