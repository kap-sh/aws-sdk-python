"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AttachmentStatus``."""

from typing import Literal, TypeAlias, cast

AttachmentStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "FAILED",
    "ERROR",
    "SCALING",
    "READY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttachmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AttachmentStatus:
    return cast(AttachmentStatus, data)
