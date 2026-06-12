"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""A job's status can be SUBMITTED, PROGRESSING, COMPLETE, CANCELED, or ERROR."""
JobStatus: TypeAlias = Literal[
    "SUBMITTED",
    "PROGRESSING",
    "COMPLETE",
    "CANCELED",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "PROGRESSING",
        "COMPLETE",
        "CANCELED",
        "ERROR",
    )
)


def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
