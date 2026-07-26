"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

EksAnywhereSubscriptionStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "EXPIRING",
    "EXPIRED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: EksAnywhereSubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> EksAnywhereSubscriptionStatus:
    return cast(EksAnywhereSubscriptionStatus, data)
