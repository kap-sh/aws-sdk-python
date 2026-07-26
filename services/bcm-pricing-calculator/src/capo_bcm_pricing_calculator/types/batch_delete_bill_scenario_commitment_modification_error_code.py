"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteBillScenarioCommitmentModificationErrorCode``."""

from typing import Literal, TypeAlias, cast

BatchDeleteBillScenarioCommitmentModificationErrorCode: TypeAlias = Literal[
    "BAD_REQUEST",
    "CONFLICT",
    "INTERNAL_SERVER_ERROR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: BatchDeleteBillScenarioCommitmentModificationErrorCode,
) -> str:
    return value


def deserialize_aws_json_1_0(
    data: str,
) -> BatchDeleteBillScenarioCommitmentModificationErrorCode:
    return cast(BatchDeleteBillScenarioCommitmentModificationErrorCode, data)
