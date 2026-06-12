"""Generated from Smithy shape ``com.amazonaws.identitystore#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_identitystore.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "KMS_INVALID_ARN",
    "KMS_INVALID_KEY_USAGE",
    "KMS_INVALID_STATE",
    "KMS_DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KMS_INVALID_ARN",
        "KMS_INVALID_KEY_USAGE",
        "KMS_INVALID_STATE",
        "KMS_DISABLED",
    )
)


def serialize_aws_json_1_1(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
