"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionGrantOverallStatus``."""

from typing import Literal, TypeAlias, cast

SubscriptionGrantOverallStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "GRANT_FAILED",
    "REVOKE_FAILED",
    "GRANT_AND_REVOKE_FAILED",
    "COMPLETED",
    "INACCESSIBLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionGrantOverallStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionGrantOverallStatus:
    return cast(SubscriptionGrantOverallStatus, data)
