"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EncodingProfile``."""

from typing import Literal, TypeAlias, cast

EncodingProfile: TypeAlias = Literal[
    "DISTRIBUTION_H264_DEFAULT",
    "CONTRIBUTION_H264_DEFAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncodingProfile) -> str:
    return value


def deserialize_json(data: str) -> EncodingProfile:
    return cast(EncodingProfile, data)
