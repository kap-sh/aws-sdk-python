"""Generated from Smithy shape ``com.amazonaws.securitylake#SubscriberStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securitylake.errors import DeserializationError

SubscriberStatus: TypeAlias = Literal[
    "ACTIVE",
    "DEACTIVATED",
    "PENDING",
    "READY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DEACTIVATED",
        "PENDING",
        "READY",
    )
)


def serialize_json(value: SubscriberStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriberStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriberStatus value: {data!r}")
    return cast(SubscriberStatus, data)
