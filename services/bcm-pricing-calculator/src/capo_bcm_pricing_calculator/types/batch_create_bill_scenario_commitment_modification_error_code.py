"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchCreateBillScenarioCommitmentModificationErrorCode: TypeAlias = Literal[
    "CONFLICT",
    "INTERNAL_SERVER_ERROR",
    "INVALID_ACCOUNT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioCommitmentModificationErrorCode,
) -> str:
    return value


def deserialize_aws_json_1_0(
    data: str,
) -> BatchCreateBillScenarioCommitmentModificationErrorCode:
    return cast(BatchCreateBillScenarioCommitmentModificationErrorCode, data)
