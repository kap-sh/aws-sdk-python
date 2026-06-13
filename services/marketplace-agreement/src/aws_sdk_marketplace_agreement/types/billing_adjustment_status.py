"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BillingAdjustmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

BillingAdjustmentStatus: TypeAlias = Literal[
    "PENDING",
    "VALIDATION_FAILED",
    "COMPLETED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "VALIDATION_FAILED",
        "COMPLETED",
    )
)


def serialize_aws_json_1_0(value: BillingAdjustmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingAdjustmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingAdjustmentStatus value: {data!r}")
    return cast(BillingAdjustmentStatus, data)
