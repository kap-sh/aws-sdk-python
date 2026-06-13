"""Generated from Smithy shape ``com.amazonaws.mailmanager#ImportJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

ImportJobStatus: TypeAlias = Literal[
    "CREATED",
    "PROCESSING",
    "COMPLETED",
    "FAILED",
    "STOPPED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
        "STOPPED",
    )
)


def serialize_aws_json_1_0(value: ImportJobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ImportJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportJobStatus value: {data!r}")
    return cast(ImportJobStatus, data)
