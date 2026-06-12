"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#HubNetworkMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

HubNetworkMode: TypeAlias = Literal[
    "STANDARD",
    "NETWORK_WIDE_EXCLUSION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "NETWORK_WIDE_EXCLUSION",
    )
)


def serialize_json(value: HubNetworkMode) -> str:
    return value


def deserialize_json(data: str) -> HubNetworkMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HubNetworkMode value: {data!r}")
    return cast(HubNetworkMode, data)
