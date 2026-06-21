"""Generated from Smithy shape ``com.amazonaws.ssooidc#InvalidRequestExceptionReason``."""

from typing import Literal, TypeAlias, cast

InvalidRequestExceptionReason: TypeAlias = Literal[
    "KMS_NotFoundException",
    "KMS_InvalidKeyUsageException",
    "KMS_InvalidStateException",
    "KMS_DisabledException",
]


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> InvalidRequestExceptionReason:
    return cast(InvalidRequestExceptionReason, data)
