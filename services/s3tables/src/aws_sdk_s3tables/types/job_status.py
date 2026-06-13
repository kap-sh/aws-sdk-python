"""Generated from Smithy shape ``com.amazonaws.s3tables#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

JobStatus: TypeAlias = Literal[
    "Not_Yet_Run",
    "Successful",
    "Failed",
    "Disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Not_Yet_Run",
        "Successful",
        "Failed",
        "Disabled",
    )
)


def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
