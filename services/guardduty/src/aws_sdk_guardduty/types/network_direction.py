"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

NetworkDirection: TypeAlias = Literal[
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


def serialize_json(value: NetworkDirection) -> str:
    return value


def deserialize_json(data: str) -> NetworkDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkDirection value: {data!r}")
    return cast(NetworkDirection, data)
