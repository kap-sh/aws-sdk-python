"""Generated from Smithy shape ``com.amazonaws.shield#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "FIELD_VALIDATION_FAILED",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIELD_VALIDATION_FAILED",
        "OTHER",
    )
)


def serialize_aws_json_1_1(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
