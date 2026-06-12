"""Generated from Smithy shape ``com.amazonaws.identitystore#ThrottlingExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_identitystore.errors import DeserializationError

ThrottlingExceptionReason: TypeAlias = Literal["KMS_THROTTLING",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KMS_THROTTLING",))


def serialize_aws_json_1_1(value: ThrottlingExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThrottlingExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThrottlingExceptionReason value: {data!r}")
    return cast(ThrottlingExceptionReason, data)
