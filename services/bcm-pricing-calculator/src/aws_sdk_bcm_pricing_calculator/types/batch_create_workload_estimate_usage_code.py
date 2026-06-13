"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateWorkloadEstimateUsageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

BatchCreateWorkloadEstimateUsageCode: TypeAlias = Literal[
    "BAD_REQUEST",
    "NOT_FOUND",
    "CONFLICT",
    "INTERNAL_SERVER_ERROR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BAD_REQUEST",
        "NOT_FOUND",
        "CONFLICT",
        "INTERNAL_SERVER_ERROR",
    )
)


def serialize_aws_json_1_0(value: BatchCreateWorkloadEstimateUsageCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchCreateWorkloadEstimateUsageCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchCreateWorkloadEstimateUsageCode value: {data!r}"
        )
    return cast(BatchCreateWorkloadEstimateUsageCode, data)
