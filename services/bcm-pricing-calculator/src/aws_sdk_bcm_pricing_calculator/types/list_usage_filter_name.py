"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#ListUsageFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

ListUsageFilterName: TypeAlias = Literal[
    "USAGE_ACCOUNT_ID",
    "SERVICE_CODE",
    "USAGE_TYPE",
    "OPERATION",
    "LOCATION",
    "USAGE_GROUP",
    "HISTORICAL_USAGE_ACCOUNT_ID",
    "HISTORICAL_SERVICE_CODE",
    "HISTORICAL_USAGE_TYPE",
    "HISTORICAL_OPERATION",
    "HISTORICAL_LOCATION",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USAGE_ACCOUNT_ID",
        "SERVICE_CODE",
        "USAGE_TYPE",
        "OPERATION",
        "LOCATION",
        "USAGE_GROUP",
        "HISTORICAL_USAGE_ACCOUNT_ID",
        "HISTORICAL_SERVICE_CODE",
        "HISTORICAL_USAGE_TYPE",
        "HISTORICAL_OPERATION",
        "HISTORICAL_LOCATION",
    )
)


def serialize_aws_json_1_0(value: ListUsageFilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListUsageFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ListUsageFilterName value: {data!r}")
    return cast(ListUsageFilterName, data)
