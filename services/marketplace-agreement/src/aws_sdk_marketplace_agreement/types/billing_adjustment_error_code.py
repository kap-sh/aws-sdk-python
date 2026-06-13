"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BillingAdjustmentErrorCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

BillingAdjustmentErrorCode: TypeAlias = Literal[
    "CONFLICT_EXCEPTION",
    "VALIDATION_EXCEPTION",
    "RESOURCE_NOT_FOUND_EXCEPTION",
    "INTERNAL_FAILURE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONFLICT_EXCEPTION",
        "VALIDATION_EXCEPTION",
        "RESOURCE_NOT_FOUND_EXCEPTION",
        "INTERNAL_FAILURE",
    )
)


def serialize_aws_json_1_0(value: BillingAdjustmentErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingAdjustmentErrorCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BillingAdjustmentErrorCode value: {data!r}"
        )
    return cast(BillingAdjustmentErrorCode, data)
