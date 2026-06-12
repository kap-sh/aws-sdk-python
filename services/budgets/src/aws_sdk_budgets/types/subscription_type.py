"""Generated from Smithy shape ``com.amazonaws.budgets#SubscriptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

"""<p> The subscription type of the subscriber. It can be SMS or EMAIL.</p>"""
SubscriptionType: TypeAlias = Literal[
    "SNS",
    "EMAIL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SNS",
        "EMAIL",
    )
)


def serialize_aws_json_1_1(value: SubscriptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubscriptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionType value: {data!r}")
    return cast(SubscriptionType, data)
