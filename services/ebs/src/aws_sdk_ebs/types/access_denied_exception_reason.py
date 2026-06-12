"""Generated from Smithy shape ``com.amazonaws.ebs#AccessDeniedExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ebs.errors import DeserializationError

AccessDeniedExceptionReason: TypeAlias = Literal[
    "UNAUTHORIZED_ACCOUNT",
    "DEPENDENCY_ACCESS_DENIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNAUTHORIZED_ACCOUNT",
        "DEPENDENCY_ACCESS_DENIED",
    )
)


def serialize_json(value: AccessDeniedExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> AccessDeniedExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AccessDeniedExceptionReason value: {data!r}"
        )
    return cast(AccessDeniedExceptionReason, data)
