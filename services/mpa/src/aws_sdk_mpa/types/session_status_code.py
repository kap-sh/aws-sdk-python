"""Generated from Smithy shape ``com.amazonaws.mpa#SessionStatusCode``."""

from typing import Literal, TypeAlias, cast

SessionStatusCode: TypeAlias = Literal[
    "REJECTED",
    "EXPIRED",
    "CONFIGURATION_CHANGED",
    "ALL_APPROVERS_IN_SESSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionStatusCode) -> str:
    return value


def deserialize_json(data: str) -> SessionStatusCode:
    return cast(SessionStatusCode, data)
