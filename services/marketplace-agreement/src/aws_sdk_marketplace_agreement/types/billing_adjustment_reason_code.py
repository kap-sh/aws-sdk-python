"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BillingAdjustmentReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

BillingAdjustmentReasonCode: TypeAlias = Literal[
    "INCORRECT_TERMS_ACCEPTED",
    "INCORRECT_METERING",
    "TEST_ENVIRONMENT_CHARGES",
    "ALTERNATIVE_PROCUREMENT_CHANNEL",
    "UNINTENDED_RENEWAL",
    "BUYER_DISSATISFACTION",
    "OTHER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCORRECT_TERMS_ACCEPTED",
        "INCORRECT_METERING",
        "TEST_ENVIRONMENT_CHARGES",
        "ALTERNATIVE_PROCUREMENT_CHANNEL",
        "UNINTENDED_RENEWAL",
        "BUYER_DISSATISFACTION",
        "OTHER",
    )
)


def serialize_aws_json_1_0(value: BillingAdjustmentReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingAdjustmentReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown BillingAdjustmentReasonCode value: {data!r}"
        )
    return cast(BillingAdjustmentReasonCode, data)
