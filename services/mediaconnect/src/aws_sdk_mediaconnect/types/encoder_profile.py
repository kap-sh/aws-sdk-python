"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EncoderProfile``."""

from typing import Literal, TypeAlias, cast

EncoderProfile: TypeAlias = Literal[
    "main",
    "high",
]


# --- restJson1 ser/de ---
def serialize_json(value: EncoderProfile) -> str:
    return value


def deserialize_json(data: str) -> EncoderProfile:
    return cast(EncoderProfile, data)
