"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalySubscriptionFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

AnomalySubscriptionFrequency: TypeAlias = Literal[
    "DAILY",
    "IMMEDIATE",
    "WEEKLY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAILY",
        "IMMEDIATE",
        "WEEKLY",
    )
)


def serialize_aws_json_1_1(value: AnomalySubscriptionFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnomalySubscriptionFrequency:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AnomalySubscriptionFrequency value: {data!r}"
        )
    return cast(AnomalySubscriptionFrequency, data)
