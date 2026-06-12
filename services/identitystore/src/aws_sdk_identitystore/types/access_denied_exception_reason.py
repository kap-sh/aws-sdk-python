"""Generated from Smithy shape ``com.amazonaws.identitystore#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_identitystore.errors import DeserializationError

AccessDeniedExceptionReason: TypeAlias = Literal["KMS_ACCESS_DENIED",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KMS_ACCESS_DENIED",))


def serialize_aws_json_1_1(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessDeniedExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AccessDeniedExceptionReason value: {data!r}"
        )
    return cast(AccessDeniedExceptionReason, data)
