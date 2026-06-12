"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConnectorEventOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

ConnectorEventOperation: TypeAlias = Literal[
    "DEVICE_COMMAND_RESPONSE",
    "DEVICE_DISCOVERY",
    "DEVICE_EVENT",
    "DEVICE_COMMAND_REQUEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEVICE_COMMAND_RESPONSE",
        "DEVICE_DISCOVERY",
        "DEVICE_EVENT",
        "DEVICE_COMMAND_REQUEST",
    )
)


def serialize_json(value: ConnectorEventOperation) -> str:
    return value


def deserialize_json(data: str) -> ConnectorEventOperation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorEventOperation value: {data!r}")
    return cast(ConnectorEventOperation, data)
