"""Generated from Smithy shape ``com.amazonaws.databrew#JobRunState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

JobRunState: TypeAlias = Literal[
    "STARTING",
    "RUNNING",
    "STOPPING",
    "STOPPED",
    "SUCCEEDED",
    "FAILED",
    "TIMEOUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STARTING",
        "RUNNING",
        "STOPPING",
        "STOPPED",
        "SUCCEEDED",
        "FAILED",
        "TIMEOUT",
    )
)


def serialize_json(value: JobRunState) -> str:
    return value


def deserialize_json(data: str) -> JobRunState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobRunState value: {data!r}")
    return cast(JobRunState, data)
