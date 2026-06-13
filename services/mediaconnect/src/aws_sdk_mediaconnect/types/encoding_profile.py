"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EncodingProfile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

EncodingProfile: TypeAlias = Literal[
    "DISTRIBUTION_H264_DEFAULT",
    "CONTRIBUTION_H264_DEFAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISTRIBUTION_H264_DEFAULT",
        "CONTRIBUTION_H264_DEFAULT",
    )
)


def serialize_json(value: EncodingProfile) -> str:
    return value


def deserialize_json(data: str) -> EncodingProfile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncodingProfile value: {data!r}")
    return cast(EncodingProfile, data)
