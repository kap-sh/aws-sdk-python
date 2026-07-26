"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeConstraintViolationExceptionReason``."""

from typing import Literal, TypeAlias, cast

HandshakeConstraintViolationExceptionReason: TypeAlias = Literal[
    "ACCOUNT_NUMBER_LIMIT_EXCEEDED",
    "HANDSHAKE_RATE_LIMIT_EXCEEDED",
    "ALREADY_IN_AN_ORGANIZATION",
    "ORGANIZATION_ALREADY_HAS_ALL_FEATURES",
    "ORGANIZATION_IS_ALREADY_PENDING_ALL_FEATURES_MIGRATION",
    "INVITE_DISABLED_DURING_ENABLE_ALL_FEATURES",
    "PAYMENT_INSTRUMENT_REQUIRED",
    "ORGANIZATION_FROM_DIFFERENT_SELLER_OF_RECORD",
    "ORGANIZATION_MEMBERSHIP_CHANGE_RATE_LIMIT_EXCEEDED",
    "MANAGEMENT_ACCOUNT_EMAIL_NOT_VERIFIED",
    "RESPONSIBILITY_TRANSFER_ALREADY_EXISTS",
    "SOURCE_AND_TARGET_CANNOT_MATCH",
    "UNUSED_PREPAYMENT_BALANCE",
    "LEGACY_PERMISSIONS_STILL_IN_USE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandshakeConstraintViolationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HandshakeConstraintViolationExceptionReason:
    return cast(HandshakeConstraintViolationExceptionReason, data)
