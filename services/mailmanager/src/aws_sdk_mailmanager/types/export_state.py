"""Generated from Smithy shape ``com.amazonaws.mailmanager#ExportState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

ExportState: TypeAlias = Literal[
    "QUEUED",
    "PREPROCESSING",
    "PROCESSING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "PREPROCESSING",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
    )
)


def serialize_aws_json_1_0(value: ExportState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExportState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExportState value: {data!r}")
    return cast(ExportState, data)
