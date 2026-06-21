"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionGrantStatus``."""

from typing import Literal, TypeAlias, cast

SubscriptionGrantStatus: TypeAlias = Literal[
    "GRANT_PENDING",
    "REVOKE_PENDING",
    "GRANT_IN_PROGRESS",
    "REVOKE_IN_PROGRESS",
    "GRANTED",
    "REVOKED",
    "GRANT_FAILED",
    "REVOKE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionGrantStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionGrantStatus:
    return cast(SubscriptionGrantStatus, data)
