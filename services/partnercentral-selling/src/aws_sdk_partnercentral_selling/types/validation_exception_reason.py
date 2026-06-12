"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "REQUEST_VALIDATION_FAILED",
    "BUSINESS_VALIDATION_FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUEST_VALIDATION_FAILED",
        "BUSINESS_VALIDATION_FAILED",
    )
)


def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
