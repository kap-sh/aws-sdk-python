"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConnectorEventOperation``."""

from typing import Literal, TypeAlias, cast

ConnectorEventOperation: TypeAlias = Literal[
    "DEVICE_COMMAND_RESPONSE",
    "DEVICE_DISCOVERY",
    "DEVICE_EVENT",
    "DEVICE_COMMAND_REQUEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorEventOperation) -> str:
    return value


def deserialize_json(data: str) -> ConnectorEventOperation:
    return cast(ConnectorEventOperation, data)
