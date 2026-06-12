"""Generated from Smithy shape ``com.amazonaws.mediaconvert#JobsQueryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""A job query's status can be SUBMITTED, PROGRESSING, COMPLETE, or ERROR."""
JobsQueryStatus: TypeAlias = Literal[
    "SUBMITTED",
    "PROGRESSING",
    "COMPLETE",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "PROGRESSING",
        "COMPLETE",
        "ERROR",
    )
)


def serialize_json(value: JobsQueryStatus) -> str:
    return value


def deserialize_json(data: str) -> JobsQueryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobsQueryStatus value: {data!r}")
    return cast(JobsQueryStatus, data)
