"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

ImportStatus: TypeAlias = Literal[
    "INITIALIZING",
    "IN_PROGRESS",
    "FAILED",
    "STOPPED",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZING",
        "IN_PROGRESS",
        "FAILED",
        "STOPPED",
        "COMPLETED",
    )
)


def serialize_aws_json_1_1(value: ImportStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportStatus value: {data!r}")
    return cast(ImportStatus, data)
