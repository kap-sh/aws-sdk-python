"""Generated from Smithy shape ``com.amazonaws.mpa#SessionResponse``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

SessionResponse: TypeAlias = Literal[
    "APPROVED",
    "REJECTED",
    "NO_RESPONSE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVED",
        "REJECTED",
        "NO_RESPONSE",
    )
)


def serialize_json(value: SessionResponse) -> str:
    return value


def deserialize_json(data: str) -> SessionResponse:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionResponse value: {data!r}")
    return cast(SessionResponse, data)
