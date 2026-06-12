"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobPhase``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""A job's phase can be PROBING, TRANSCODING OR UPLOADING"""
JobPhase: TypeAlias = Literal[
    "PROBING",
    "TRANSCODING",
    "UPLOADING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROBING",
        "TRANSCODING",
        "UPLOADING",
    )
)


def serialize_json(value: JobPhase) -> str:
    return value


def deserialize_json(data: str) -> JobPhase:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobPhase value: {data!r}")
    return cast(JobPhase, data)
