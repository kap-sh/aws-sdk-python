"""Generated from Smithy shape ``com.amazonaws.shield#SubscriptionState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

SubscriptionState: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_1(value: SubscriptionState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubscriptionState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionState value: {data!r}")
    return cast(SubscriptionState, data)
