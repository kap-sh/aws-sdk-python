"""Generated from Smithy shape ``com.amazonaws.mpa#SessionStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mpa.errors import DeserializationError

SessionStatusCode: TypeAlias = Literal[
    "REJECTED",
    "EXPIRED",
    "CONFIGURATION_CHANGED",
    "ALL_APPROVERS_IN_SESSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REJECTED",
        "EXPIRED",
        "CONFIGURATION_CHANGED",
        "ALL_APPROVERS_IN_SESSION",
    )
)


def serialize_json(value: SessionStatusCode) -> str:
    return value


def deserialize_json(data: str) -> SessionStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SessionStatusCode value: {data!r}")
    return cast(SessionStatusCode, data)
