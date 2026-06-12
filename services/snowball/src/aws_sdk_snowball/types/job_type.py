"""Generated from Smithy shape ``com.amazonaws.snowball#JobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

JobType: TypeAlias = Literal[
    "IMPORT",
    "EXPORT",
    "LOCAL_USE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMPORT",
        "EXPORT",
        "LOCAL_USE",
    )
)


def serialize_aws_json_1_1(value: JobType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobType value: {data!r}")
    return cast(JobType, data)
