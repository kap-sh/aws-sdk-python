"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateCostStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

WorkloadEstimateCostStatus: TypeAlias = Literal[
    "VALID",
    "INVALID",
    "STALE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALID",
        "INVALID",
        "STALE",
    )
)


def serialize_aws_json_1_0(value: WorkloadEstimateCostStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkloadEstimateCostStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkloadEstimateCostStatus value: {data!r}"
        )
    return cast(WorkloadEstimateCostStatus, data)
