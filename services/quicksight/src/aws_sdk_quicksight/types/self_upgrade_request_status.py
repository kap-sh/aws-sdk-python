"""Generated from Smithy shape ``com.amazonaws.quicksight#SelfUpgradeRequestStatus``."""

from typing import Literal, TypeAlias, cast

SelfUpgradeRequestStatus: TypeAlias = Literal[
    "PENDING",
    "APPROVED",
    "DENIED",
    "UPDATE_FAILED",
    "VERIFY_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SelfUpgradeRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> SelfUpgradeRequestStatus:
    return cast(SelfUpgradeRequestStatus, data)
