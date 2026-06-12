"""Generated from Smithy shape ``com.amazonaws.macie2#JobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The schedule for running a classification job. Valid values are:</p>"""
JobType: TypeAlias = Literal[
    "ONE_TIME",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ONE_TIME",
        "SCHEDULED",
    )
)


def serialize_json(value: JobType) -> str:
    return value


def deserialize_json(data: str) -> JobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobType value: {data!r}")
    return cast(JobType, data)
