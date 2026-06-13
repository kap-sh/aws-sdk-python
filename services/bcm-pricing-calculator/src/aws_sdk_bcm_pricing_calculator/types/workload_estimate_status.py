"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#WorkloadEstimateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

WorkloadEstimateStatus: TypeAlias = Literal[
    "UPDATING",
    "VALID",
    "INVALID",
    "ACTION_NEEDED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UPDATING",
        "VALID",
        "INVALID",
        "ACTION_NEEDED",
    )
)


def serialize_aws_json_1_0(value: WorkloadEstimateStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> WorkloadEstimateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkloadEstimateStatus value: {data!r}")
    return cast(WorkloadEstimateStatus, data)
