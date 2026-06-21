"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteBillScenarioUsageModificationErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchDeleteBillScenarioUsageModificationErrorCode: TypeAlias = Literal[
    "BAD_REQUEST",
    "CONFLICT",
    "INTERNAL_SERVER_ERROR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchDeleteBillScenarioUsageModificationErrorCode,
) -> str:
    return value


def deserialize_aws_json_1_0(
    data: str,
) -> BatchDeleteBillScenarioUsageModificationErrorCode:
    return cast(BatchDeleteBillScenarioUsageModificationErrorCode, data)
