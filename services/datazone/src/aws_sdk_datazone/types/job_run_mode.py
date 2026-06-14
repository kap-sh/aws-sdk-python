"""Generated from Smithy shape ``com.amazonaws.datazone#JobRunMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

JobRunMode: TypeAlias = Literal[
    "SCHEDULED",
    "ON_DEMAND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "ON_DEMAND",
    )
)


def serialize_json(value: JobRunMode) -> str:
    return value


def deserialize_json(data: str) -> JobRunMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobRunMode value: {data!r}")
    return cast(JobRunMode, data)
