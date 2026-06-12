"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServerSideEncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

ServerSideEncryptionType: TypeAlias = Literal[
    "CUSTOMER_MANAGED_KEY",
    "AWS_OWNED_KMS_KEY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_MANAGED_KEY",
        "AWS_OWNED_KMS_KEY",
    )
)


def serialize_json(value: ServerSideEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> ServerSideEncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServerSideEncryptionType value: {data!r}")
    return cast(ServerSideEncryptionType, data)
