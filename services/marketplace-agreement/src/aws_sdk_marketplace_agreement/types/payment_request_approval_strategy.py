"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PaymentRequestApprovalStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

PaymentRequestApprovalStrategy: TypeAlias = Literal[
    "AUTO_APPROVE_ON_EXPIRATION",
    "WAIT_FOR_APPROVAL",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO_APPROVE_ON_EXPIRATION",
        "WAIT_FOR_APPROVAL",
    )
)


def serialize_aws_json_1_0(value: PaymentRequestApprovalStrategy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PaymentRequestApprovalStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PaymentRequestApprovalStrategy value: {data!r}"
        )
    return cast(PaymentRequestApprovalStrategy, data)
