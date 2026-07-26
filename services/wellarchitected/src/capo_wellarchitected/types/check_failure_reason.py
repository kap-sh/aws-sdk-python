"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckFailureReason``."""

from typing import Literal, TypeAlias, cast

CheckFailureReason: TypeAlias = Literal[
    "ASSUME_ROLE_ERROR",
    "ACCESS_DENIED",
    "UNKNOWN_ERROR",
    "PREMIUM_SUPPORT_REQUIRED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CheckFailureReason) -> str:
    return value


def deserialize_json(data: str) -> CheckFailureReason:
    return cast(CheckFailureReason, data)
