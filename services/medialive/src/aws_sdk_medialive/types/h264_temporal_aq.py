"""Generated from Smithy shape ``com.amazonaws.medialive#H264TemporalAq``."""

from typing import Literal, TypeAlias, cast

"""H264 Temporal Aq"""
H264TemporalAq: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264TemporalAq) -> str:
    return value


def deserialize_json(data: str) -> H264TemporalAq:
    return cast(H264TemporalAq, data)
