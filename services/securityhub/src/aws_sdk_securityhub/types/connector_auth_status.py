"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectorAuthStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ConnectorAuthStatus: TypeAlias = Literal[
    "ACTIVE",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "FAILED",
    )
)


def serialize_json(value: ConnectorAuthStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectorAuthStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorAuthStatus value: {data!r}")
    return cast(ConnectorAuthStatus, data)
