"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

NetworkDirection: TypeAlias = Literal[
    "IN",
    "OUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN",
        "OUT",
    )
)


def serialize_json(value: NetworkDirection) -> str:
    return value


def deserialize_json(data: str) -> NetworkDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkDirection value: {data!r}")
    return cast(NetworkDirection, data)
