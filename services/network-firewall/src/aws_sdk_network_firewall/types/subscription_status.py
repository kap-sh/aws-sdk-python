"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SubscriptionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_network_firewall.errors import DeserializationError

SubscriptionStatus: TypeAlias = Literal[
    "NOT_SUBSCRIBED",
    "SUBSCRIBED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_SUBSCRIBED",
        "SUBSCRIBED",
    )
)


def serialize_aws_json_1_0(value: SubscriptionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SubscriptionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionStatus value: {data!r}")
    return cast(SubscriptionStatus, data)
