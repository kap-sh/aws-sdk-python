"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckFailureReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

CheckFailureReason: TypeAlias = Literal[
    "ASSUME_ROLE_ERROR",
    "ACCESS_DENIED",
    "UNKNOWN_ERROR",
    "PREMIUM_SUPPORT_REQUIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSUME_ROLE_ERROR",
        "ACCESS_DENIED",
        "UNKNOWN_ERROR",
        "PREMIUM_SUPPORT_REQUIRED",
    )
)


def serialize_json(value: CheckFailureReason) -> str:
    return value


def deserialize_json(data: str) -> CheckFailureReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CheckFailureReason value: {data!r}")
    return cast(CheckFailureReason, data)
