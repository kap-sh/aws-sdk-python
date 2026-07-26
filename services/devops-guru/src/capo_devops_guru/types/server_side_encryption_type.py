"""Generated from Smithy shape ``com.amazonaws.devopsguru#ServerSideEncryptionType``."""

from typing import Literal, TypeAlias, cast

ServerSideEncryptionType: TypeAlias = Literal[
    "CUSTOMER_MANAGED_KEY",
    "AWS_OWNED_KMS_KEY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServerSideEncryptionType) -> str:
    return value


def deserialize_json(data: str) -> ServerSideEncryptionType:
    return cast(ServerSideEncryptionType, data)
