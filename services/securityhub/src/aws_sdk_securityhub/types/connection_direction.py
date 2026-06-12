"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectionDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ConnectionDirection: TypeAlias = Literal[
    "INBOUND",
    "OUTBOUND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INBOUND",
        "OUTBOUND",
    )
)


def serialize_json(value: ConnectionDirection) -> str:
    return value


def deserialize_json(data: str) -> ConnectionDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectionDirection value: {data!r}")
    return cast(ConnectionDirection, data)
