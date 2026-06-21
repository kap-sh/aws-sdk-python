"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectorStatus``."""

from typing import Literal, TypeAlias, cast

ConnectorStatus: TypeAlias = Literal[
    "CONNECTED",
    "FAILED_TO_CONNECT",
    "PENDING_CONFIGURATION",
    "PENDING_AUTHORIZATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectorStatus:
    return cast(ConnectorStatus, data)
