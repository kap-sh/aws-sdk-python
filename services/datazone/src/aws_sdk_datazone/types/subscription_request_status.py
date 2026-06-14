"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionRequestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

SubscriptionRequestStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "REJECTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ACCEPTED",
        "REJECTED",
    )
)


def serialize_json(value: SubscriptionRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionRequestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionRequestStatus value: {data!r}")
    return cast(SubscriptionRequestStatus, data)
