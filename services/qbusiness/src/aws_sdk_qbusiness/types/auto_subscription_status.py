"""Generated from Smithy shape ``com.amazonaws.qbusiness#AutoSubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

AutoSubscriptionStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: AutoSubscriptionStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoSubscriptionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoSubscriptionStatus value: {data!r}")
    return cast(AutoSubscriptionStatus, data)
