"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateRateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

WorkloadEstimateRateType: TypeAlias = Literal[
    "BEFORE_DISCOUNTS",
    "AFTER_DISCOUNTS",
    "AFTER_DISCOUNTS_AND_COMMITMENTS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BEFORE_DISCOUNTS",
        "AFTER_DISCOUNTS",
        "AFTER_DISCOUNTS_AND_COMMITMENTS",
    )
)


def serialize_aws_json_1_0(value: WorkloadEstimateRateType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkloadEstimateRateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkloadEstimateRateType value: {data!r}")
    return cast(WorkloadEstimateRateType, data)
