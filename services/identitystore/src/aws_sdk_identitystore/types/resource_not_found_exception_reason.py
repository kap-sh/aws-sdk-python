"""Generated from Smithy shape ``com.amazonaws.identitystore#ResourceNotFoundExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_identitystore.errors import DeserializationError

ResourceNotFoundExceptionReason: TypeAlias = Literal["KMS_KEY_NOT_FOUND",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KMS_KEY_NOT_FOUND",))


def serialize_aws_json_1_1(value: ResourceNotFoundExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceNotFoundExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceNotFoundExceptionReason value: {data!r}"
        )
    return cast(ResourceNotFoundExceptionReason, data)
