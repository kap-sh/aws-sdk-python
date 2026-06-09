"""Generated from Smithy shape ``com.amazonaws.eks#EksAnywhereSubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

EksAnywhereSubscriptionStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "EXPIRING",
    "EXPIRED",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "EXPIRING",
        "EXPIRED",
        "DELETING",
    )
)


def serialize_json(value: EksAnywhereSubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> EksAnywhereSubscriptionStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EksAnywhereSubscriptionStatus value: {data!r}"
        )
    return cast(EksAnywhereSubscriptionStatus, data)
