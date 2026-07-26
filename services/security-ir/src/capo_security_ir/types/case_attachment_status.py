"""Generated from Smithy shape ``com.amazonaws.securityir#CaseAttachmentStatus``."""

from typing import Literal, TypeAlias, cast

CaseAttachmentStatus: TypeAlias = Literal[
    "Verified",
    "Failed",
    "Pending",
]


# --- restJson1 ser/de ---
def serialize_json(value: CaseAttachmentStatus) -> str:
    return value


def deserialize_json(data: str) -> CaseAttachmentStatus:
    return cast(CaseAttachmentStatus, data)
