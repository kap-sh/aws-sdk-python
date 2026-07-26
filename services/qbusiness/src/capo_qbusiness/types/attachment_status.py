"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentStatus``."""

from typing import Literal, TypeAlias, cast

AttachmentStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentStatus) -> str:
    return value


def deserialize_json(data: str) -> AttachmentStatus:
    return cast(AttachmentStatus, data)
