"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalySubscriptionFrequency``."""

from typing import Literal, TypeAlias, cast

AnomalySubscriptionFrequency: TypeAlias = Literal[
    "DAILY",
    "IMMEDIATE",
    "WEEKLY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalySubscriptionFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AnomalySubscriptionFrequency:
    return cast(AnomalySubscriptionFrequency, data)
