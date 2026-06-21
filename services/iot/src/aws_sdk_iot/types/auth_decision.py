"""Generated from Smithy shape ``com.amazonaws.iot#AuthDecision``."""

from typing import Literal, TypeAlias, cast

AuthDecision: TypeAlias = Literal[
    "ALLOWED",
    "EXPLICIT_DENY",
    "IMPLICIT_DENY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthDecision) -> str:
    return value


def deserialize_json(data: str) -> AuthDecision:
    return cast(AuthDecision, data)
