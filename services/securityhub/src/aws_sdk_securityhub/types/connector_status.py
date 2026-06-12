"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ConnectorStatus: TypeAlias = Literal[
    "CONNECTED",
    "FAILED_TO_CONNECT",
    "PENDING_CONFIGURATION",
    "PENDING_AUTHORIZATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONNECTED",
        "FAILED_TO_CONNECT",
        "PENDING_CONFIGURATION",
        "PENDING_AUTHORIZATION",
    )
)


def serialize_json(value: ConnectorStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorStatus value: {data!r}")
    return cast(ConnectorStatus, data)
