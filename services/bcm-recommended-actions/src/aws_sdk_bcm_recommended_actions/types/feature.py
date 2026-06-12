"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#Feature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_recommended_actions.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_0(value: Feature) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Feature:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Feature value: {data!r}")
    return cast(Feature, data)
