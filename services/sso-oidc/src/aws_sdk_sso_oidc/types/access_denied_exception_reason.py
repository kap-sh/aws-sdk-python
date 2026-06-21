"""Generated from Smithy shape ``com.amazonaws.ssooidc#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

AccessDeniedExceptionReason: TypeAlias = Literal["KMS_AccessDeniedException",]


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> AccessDeniedExceptionReason:
    return cast(AccessDeniedExceptionReason, data)
