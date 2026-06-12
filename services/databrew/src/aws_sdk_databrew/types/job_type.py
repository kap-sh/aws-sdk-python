"""Generated from Smithy shape ``com.amazonaws.databrew#JobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_databrew.errors import DeserializationError

JobType: TypeAlias = Literal[
    "PROFILE",
    "RECIPE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROFILE",
        "RECIPE",
    )
)


def serialize_json(value: JobType) -> str:
    return value


def deserialize_json(data: str) -> JobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobType value: {data!r}")
    return cast(JobType, data)
