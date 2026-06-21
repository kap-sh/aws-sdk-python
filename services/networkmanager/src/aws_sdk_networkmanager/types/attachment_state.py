"""Generated from Smithy shape ``com.amazonaws.networkmanager#AttachmentState``."""

from typing import Literal, TypeAlias, cast

AttachmentState: TypeAlias = Literal[
    "REJECTED",
    "PENDING_ATTACHMENT_ACCEPTANCE",
    "CREATING",
    "FAILED",
    "AVAILABLE",
    "UPDATING",
    "PENDING_NETWORK_UPDATE",
    "PENDING_TAG_ACCEPTANCE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentState) -> str:
    return value


def deserialize_json(data: str) -> AttachmentState:
    return cast(AttachmentState, data)
