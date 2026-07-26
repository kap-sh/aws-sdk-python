"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#Feature``."""

from typing import Literal, TypeAlias, cast

Feature: TypeAlias = Literal[
    "ACCOUNT",
    "BUDGETS",
    "COST_ANOMALY_DETECTION",
    "COST_OPTIMIZATION_HUB",
    "FREE_TIER",
    "IAM",
    "PAYMENTS",
    "RESERVATIONS",
    "SAVINGS_PLANS",
    "TAX_SETTINGS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Feature) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Feature:
    return cast(Feature, data)
