"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

AccessDeniedExceptionReason: TypeAlias = Literal["KMS_AccessDeniedException",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KMS_AccessDeniedException",))


def serialize_aws_json_1_1(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessDeniedExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AccessDeniedExceptionReason value: {data!r}"
        )
    return cast(AccessDeniedExceptionReason, data)
