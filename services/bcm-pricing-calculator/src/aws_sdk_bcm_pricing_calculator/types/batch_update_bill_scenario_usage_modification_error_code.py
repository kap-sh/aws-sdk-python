"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateBillScenarioUsageModificationErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchUpdateBillScenarioUsageModificationErrorCode: TypeAlias = Literal[
    "BAD_REQUEST",
    "NOT_FOUND",
    "CONFLICT",
    "INTERNAL_SERVER_ERROR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchUpdateBillScenarioUsageModificationErrorCode,
) -> str:
    return value


def deserialize_aws_json_1_0(
    data: str,
) -> BatchUpdateBillScenarioUsageModificationErrorCode:
    return cast(BatchUpdateBillScenarioUsageModificationErrorCode, data)
