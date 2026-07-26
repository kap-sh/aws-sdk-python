"""Generated from Smithy shape ``com.amazonaws.medialive#ConnectionMode``."""

from typing import Literal, TypeAlias, cast

"""Placeholder documentation for ConnectionMode"""
ConnectionMode: TypeAlias = Literal[
    "CALLER",
    "LISTENER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionMode) -> str:
    return value


def deserialize_json(data: str) -> ConnectionMode:
    return cast(ConnectionMode, data)
