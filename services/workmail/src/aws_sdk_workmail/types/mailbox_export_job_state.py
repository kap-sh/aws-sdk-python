"""Generated from Smithy shape ``com.amazonaws.workmail#MailboxExportJobState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

MailboxExportJobState: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
    )
)


def serialize_aws_json_1_1(value: MailboxExportJobState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MailboxExportJobState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MailboxExportJobState value: {data!r}")
    return cast(MailboxExportJobState, data)
