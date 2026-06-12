"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "KMS_InvalidKeyUsageException",
    "KMS_InvalidStateException",
    "KMS_DisabledException",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KMS_InvalidKeyUsageException",
        "KMS_InvalidStateException",
        "KMS_DisabledException",
    )
)


def serialize_aws_json_1_1(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
