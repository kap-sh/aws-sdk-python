"""Generated from Smithy shape ``com.amazonaws.workmail#MailboxExportJobState``."""

from typing import Literal, TypeAlias, cast

MailboxExportJobState: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MailboxExportJobState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MailboxExportJobState:
    return cast(MailboxExportJobState, data)
