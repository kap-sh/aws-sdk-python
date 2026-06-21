"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryStateReasonCode``."""

from typing import Literal, TypeAlias, cast

CanaryStateReasonCode: TypeAlias = Literal[
    "INVALID_PERMISSIONS",
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "UPDATE_PENDING",
    "UPDATE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "ROLLBACK_COMPLETE",
    "ROLLBACK_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
    "SYNC_DELETE_IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CanaryStateReasonCode) -> str:
    return value


def deserialize_json(data: str) -> CanaryStateReasonCode:
    return cast(CanaryStateReasonCode, data)
