"""Generated from Smithy shape ``com.amazonaws.cleanrooms#JobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

JobType: TypeAlias = Literal[
    "BATCH",
    "INCREMENTAL",
    "DELETE_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BATCH",
        "INCREMENTAL",
        "DELETE_ONLY",
    )
)


def serialize_json(value: JobType) -> str:
    return value


def deserialize_json(data: str) -> JobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobType value: {data!r}")
    return cast(JobType, data)
