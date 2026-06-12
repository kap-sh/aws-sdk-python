"""Generated from Smithy shape ``com.amazonaws.iot#AuthDecision``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AuthDecision: TypeAlias = Literal[
    "ALLOWED",
    "EXPLICIT_DENY",
    "IMPLICIT_DENY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOWED",
        "EXPLICIT_DENY",
        "IMPLICIT_DENY",
    )
)


def serialize_json(value: AuthDecision) -> str:
    return value


def deserialize_json(data: str) -> AuthDecision:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthDecision value: {data!r}")
    return cast(AuthDecision, data)
