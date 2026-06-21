"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobPhase``."""

from typing import Literal, TypeAlias, cast

"""A job's phase can be PROBING, TRANSCODING OR UPLOADING"""
JobPhase: TypeAlias = Literal[
    "PROBING",
    "TRANSCODING",
    "UPLOADING",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobPhase) -> str:
    return value


def deserialize_json(data: str) -> JobPhase:
    return cast(JobPhase, data)
