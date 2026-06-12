"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#JobState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_reviewer.errors import DeserializationError

JobState: TypeAlias = Literal[
    "Completed",
    "Pending",
    "Failed",
    "Deleting",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Completed",
        "Pending",
        "Failed",
        "Deleting",
    )
)


def serialize_json(value: JobState) -> str:
    return value


def deserialize_json(data: str) -> JobState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobState value: {data!r}")
    return cast(JobState, data)
