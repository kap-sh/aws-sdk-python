"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PaymentRequestStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

PaymentRequestStatus: TypeAlias = Literal[
    "VALIDATING",
    "VALIDATION_FAILED",
    "PENDING_APPROVAL",
    "APPROVED",
    "REJECTED",
    "CANCELLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALIDATING",
        "VALIDATION_FAILED",
        "PENDING_APPROVAL",
        "APPROVED",
        "REJECTED",
        "CANCELLED",
    )
)


def serialize_aws_json_1_0(value: PaymentRequestStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PaymentRequestStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PaymentRequestStatus value: {data!r}")
    return cast(PaymentRequestStatus, data)
