"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteBillScenarioCommitmentModificationErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

BatchDeleteBillScenarioCommitmentModificationErrorCode: TypeAlias = Literal[
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
    value: BatchDeleteBillScenarioCommitmentModificationErrorCode,
) -> str:
    return value


def deserialize_aws_json_1_0(
    data: str,
) -> BatchDeleteBillScenarioCommitmentModificationErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchDeleteBillScenarioCommitmentModificationErrorCode value: {data!r}"
        )
    return cast(BatchDeleteBillScenarioCommitmentModificationErrorCode, data)
