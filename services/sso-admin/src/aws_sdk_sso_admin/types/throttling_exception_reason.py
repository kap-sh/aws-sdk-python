"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ThrottlingExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

ThrottlingExceptionReason: TypeAlias = Literal["KMS_ThrottlingException",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KMS_ThrottlingException",))


def serialize_aws_json_1_1(value: ThrottlingExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThrottlingExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThrottlingExceptionReason value: {data!r}")
    return cast(ThrottlingExceptionReason, data)
