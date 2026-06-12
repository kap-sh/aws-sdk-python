"""Generated from Smithy shape ``com.amazonaws.budgets#HealthStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_budgets.errors import DeserializationError

HealthStatusReason: TypeAlias = Literal[
    "BILLING_VIEW_NO_ACCESS",
    "BILLING_VIEW_UNHEALTHY",
    "FILTER_INVALID",
    "MULTI_YEAR_HISTORICAL_DATA_DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BILLING_VIEW_NO_ACCESS",
        "BILLING_VIEW_UNHEALTHY",
        "FILTER_INVALID",
        "MULTI_YEAR_HISTORICAL_DATA_DISABLED",
    )
)


def serialize_aws_json_1_1(value: HealthStatusReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HealthStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HealthStatusReason value: {data!r}")
    return cast(HealthStatusReason, data)
