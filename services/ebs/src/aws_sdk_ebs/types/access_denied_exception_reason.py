"""Generated from Smithy shape ``com.amazonaws.ebs#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

AccessDeniedExceptionReason: TypeAlias = Literal[
    "UNAUTHORIZED_ACCOUNT",
    "DEPENDENCY_ACCESS_DENIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> AccessDeniedExceptionReason:
    return cast(AccessDeniedExceptionReason, data)
