"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

BillEstimateStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "COMPLETE",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "COMPLETE",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: BillEstimateStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillEstimateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillEstimateStatus value: {data!r}")
    return cast(BillEstimateStatus, data)
