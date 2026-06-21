"""Generated from Smithy shape ``com.amazonaws.guardduty#TrustedEntitySetStatus``."""

from typing import Literal, TypeAlias, cast

TrustedEntitySetStatus: TypeAlias = Literal[
    "INACTIVE",
    "ACTIVATING",
    "ACTIVE",
    "DEACTIVATING",
    "ERROR",
    "DELETE_PENDING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrustedEntitySetStatus) -> str:
    return value


def deserialize_json(data: str) -> TrustedEntitySetStatus:
    return cast(TrustedEntitySetStatus, data)
