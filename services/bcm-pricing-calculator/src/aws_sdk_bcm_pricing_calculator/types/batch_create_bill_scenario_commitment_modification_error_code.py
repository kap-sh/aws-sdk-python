"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateBillScenarioCommitmentModificationErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

BatchCreateBillScenarioCommitmentModificationErrorCode: TypeAlias = Literal[
    "CONFLICT",
    "INTERNAL_SERVER_ERROR",
    "INVALID_ACCOUNT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONFLICT",
        "INTERNAL_SERVER_ERROR",
        "INVALID_ACCOUNT",
    )
)


def serialize_aws_json_1_0(
    value: BatchCreateBillScenarioCommitmentModificationErrorCode,
) -> str:
    return value


def deserialize_aws_json_1_0(
    data: str,
) -> BatchCreateBillScenarioCommitmentModificationErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BatchCreateBillScenarioCommitmentModificationErrorCode value: {data!r}"
        )
    return cast(BatchCreateBillScenarioCommitmentModificationErrorCode, data)
