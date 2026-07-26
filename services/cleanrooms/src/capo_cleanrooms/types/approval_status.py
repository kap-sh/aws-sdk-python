"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ApprovalStatus``."""

from typing import Literal, TypeAlias, cast

ApprovalStatus: TypeAlias = Literal[
    "APPROVED",
    "DENIED",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalStatus) -> str:
    return value


def deserialize_json(data: str) -> ApprovalStatus:
    return cast(ApprovalStatus, data)
