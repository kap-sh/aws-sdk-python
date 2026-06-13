"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteBillScenarioUsageModificationErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

BatchDeleteBillScenarioUsageModificationErrorCode: TypeAlias = Literal[
    "BAD_REQUEST",
    "CONFLICT",
    "INTERNAL_SERVER_ERROR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BAD_REQUEST",
        "CONFLICT",
        "INTERNAL_SERVER_ERROR",
    )
)


def serialize_aws_json_1_0(
    value: BatchDeleteBillScenarioUsageModificationErrorCode,
) -> str:
    return value


def deserialize_aws_json_1_0(
    data: str,
) -> BatchDeleteBillScenarioUsageModificationErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchDeleteBillScenarioUsageModificationErrorCode value: {data!r}"
        )
    return cast(BatchDeleteBillScenarioUsageModificationErrorCode, data)
