"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_agreement.errors import DeserializationError

AccessDeniedExceptionReason: TypeAlias = Literal[
    "INVALID_ACCOUNT_STATE",
    "DENIED_BY_PRIVATE_MARKETPLACE_POLICY",
    "FAILED_KYC_COMPLIANCE",
    "MISSING_MFA",
    "INVALID_ACCESS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID_ACCOUNT_STATE",
        "DENIED_BY_PRIVATE_MARKETPLACE_POLICY",
        "FAILED_KYC_COMPLIANCE",
        "MISSING_MFA",
        "INVALID_ACCESS",
    )
)


def serialize_aws_json_1_0(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccessDeniedExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AccessDeniedExceptionReason value: {data!r}"
        )
    return cast(AccessDeniedExceptionReason, data)
