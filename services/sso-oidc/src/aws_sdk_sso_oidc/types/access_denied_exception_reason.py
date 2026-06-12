"""Generated from Smithy shape ``com.amazonaws.ssooidc#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_oidc.errors import DeserializationError

AccessDeniedExceptionReason: TypeAlias = Literal["KMS_AccessDeniedException",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("KMS_AccessDeniedException",))


def serialize_json(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> AccessDeniedExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AccessDeniedExceptionReason value: {data!r}"
        )
    return cast(AccessDeniedExceptionReason, data)
