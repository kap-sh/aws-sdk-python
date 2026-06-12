"""Generated from Smithy shape ``com.amazonaws.organizations#CreateAccountFailureReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

CreateAccountFailureReason: TypeAlias = Literal[
    "ACCOUNT_LIMIT_EXCEEDED",
    "EMAIL_ALREADY_EXISTS",
    "INVALID_ADDRESS",
    "INVALID_EMAIL",
    "CONCURRENT_ACCOUNT_MODIFICATION",
    "INTERNAL_FAILURE",
    "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
    "MISSING_BUSINESS_VALIDATION",
    "FAILED_BUSINESS_VALIDATION",
    "PENDING_BUSINESS_VALIDATION",
    "INVALID_IDENTITY_FOR_BUSINESS_VALIDATION",
    "UNKNOWN_BUSINESS_VALIDATION",
    "MISSING_PAYMENT_INSTRUMENT",
    "INVALID_PAYMENT_INSTRUMENT",
    "UPDATE_EXISTING_RESOURCE_POLICY_WITH_TAGS_NOT_SUPPORTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT_LIMIT_EXCEEDED",
        "EMAIL_ALREADY_EXISTS",
        "INVALID_ADDRESS",
        "INVALID_EMAIL",
        "CONCURRENT_ACCOUNT_MODIFICATION",
        "INTERNAL_FAILURE",
        "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
        "MISSING_BUSINESS_VALIDATION",
        "FAILED_BUSINESS_VALIDATION",
        "PENDING_BUSINESS_VALIDATION",
        "INVALID_IDENTITY_FOR_BUSINESS_VALIDATION",
        "UNKNOWN_BUSINESS_VALIDATION",
        "MISSING_PAYMENT_INSTRUMENT",
        "INVALID_PAYMENT_INSTRUMENT",
        "UPDATE_EXISTING_RESOURCE_POLICY_WITH_TAGS_NOT_SUPPORTED",
    )
)


def serialize_aws_json_1_1(value: CreateAccountFailureReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CreateAccountFailureReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CreateAccountFailureReason value: {data!r}"
        )
    return cast(CreateAccountFailureReason, data)
