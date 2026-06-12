"""Generated from Smithy shape ``com.amazonaws.ssooidc#InvalidRequestExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_oidc.errors import DeserializationError

InvalidRequestExceptionReason: TypeAlias = Literal[
    "KMS_NotFoundException",
    "KMS_InvalidKeyUsageException",
    "KMS_InvalidStateException",
    "KMS_DisabledException",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KMS_NotFoundException",
        "KMS_InvalidKeyUsageException",
        "KMS_InvalidStateException",
        "KMS_DisabledException",
    )
)


def serialize_json(value: InvalidRequestExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> InvalidRequestExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InvalidRequestExceptionReason value: {data!r}"
        )
    return cast(InvalidRequestExceptionReason, data)
