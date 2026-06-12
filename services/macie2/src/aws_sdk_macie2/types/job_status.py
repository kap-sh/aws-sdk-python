"""Generated from Smithy shape ``com.amazonaws.macie2#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The status of a classification job. Possible values are:</p>"""
JobStatus: TypeAlias = Literal[
    "RUNNING",
    "PAUSED",
    "CANCELLED",
    "COMPLETE",
    "IDLE",
    "USER_PAUSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "PAUSED",
        "CANCELLED",
        "COMPLETE",
        "IDLE",
        "USER_PAUSED",
    )
)


def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
