"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioUsageModificationErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchCreateBillScenarioUsageModificationErrorCode: TypeAlias = Literal[
    "BAD_REQUEST",
    "NOT_FOUND",
    "CONFLICT",
    "INTERNAL_SERVER_ERROR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioUsageModificationErrorCode,
) -> str:
    return value


def deserialize_aws_json_1_0(
    data: str,
) -> BatchCreateBillScenarioUsageModificationErrorCode:
    return cast(BatchCreateBillScenarioUsageModificationErrorCode, data)
