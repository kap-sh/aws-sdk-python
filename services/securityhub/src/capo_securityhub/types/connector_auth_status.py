"""Generated from Smithy shape ``com.amazonaws.securityhub#ConnectorAuthStatus``."""

from typing import Literal, TypeAlias, cast

ConnectorAuthStatus: TypeAlias = Literal[
    "ACTIVE",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorAuthStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectorAuthStatus:
    return cast(ConnectorAuthStatus, data)
