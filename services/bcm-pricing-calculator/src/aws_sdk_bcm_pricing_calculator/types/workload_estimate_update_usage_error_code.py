"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateUpdateUsageErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

WorkloadEstimateUpdateUsageErrorCode: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: WorkloadEstimateUpdateUsageErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkloadEstimateUpdateUsageErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkloadEstimateUpdateUsageErrorCode value: {data!r}"
        )
    return cast(WorkloadEstimateUpdateUsageErrorCode, data)
