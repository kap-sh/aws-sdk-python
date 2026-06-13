"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementEntitlementStatusReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

AgreementEntitlementStatusReasonCode: TypeAlias = Literal[
    "PROVISIONING_IN_PROGRESS",
    "FUTURE_START_DATE",
    "INVALID_PAYMENT_INSTRUMENT",
    "INCOMPATIBLE_CURRENCY",
    "ACCOUNT_SUSPENDED",
    "UNSUPPORTED_OPERATION",
    "AGREEMENT_INACTIVE",
    "AGREEMENT_ACTIVE",
    "PRODUCT_RESTRICTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVISIONING_IN_PROGRESS",
        "FUTURE_START_DATE",
        "INVALID_PAYMENT_INSTRUMENT",
        "INCOMPATIBLE_CURRENCY",
        "ACCOUNT_SUSPENDED",
        "UNSUPPORTED_OPERATION",
        "AGREEMENT_INACTIVE",
        "AGREEMENT_ACTIVE",
        "PRODUCT_RESTRICTED",
    )
)


def serialize_aws_json_1_0(value: AgreementEntitlementStatusReasonCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementEntitlementStatusReasonCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AgreementEntitlementStatusReasonCode value: {data!r}"
        )
    return cast(AgreementEntitlementStatusReasonCode, data)
