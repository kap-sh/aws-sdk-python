"""Generated from Smithy shape ``com.amazonaws.medialive#HlsH265PackagingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Hls H265 Packaging Type"""
HlsH265PackagingType: TypeAlias = Literal[
    "HEV1",
    "HVC1",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEV1",
        "HVC1",
    )
)


def serialize_json(value: HlsH265PackagingType) -> str:
    return value


def deserialize_json(data: str) -> HlsH265PackagingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HlsH265PackagingType value: {data!r}")
    return cast(HlsH265PackagingType, data)
