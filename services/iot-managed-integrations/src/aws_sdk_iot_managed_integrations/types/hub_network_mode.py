"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#HubNetworkMode``."""

from typing import Literal, TypeAlias, cast

HubNetworkMode: TypeAlias = Literal[
    "STANDARD",
    "NETWORK_WIDE_EXCLUSION",
]


# --- restJson1 ser/de ---
def serialize_json(value: HubNetworkMode) -> str:
    return value


def deserialize_json(data: str) -> HubNetworkMode:
    return cast(HubNetworkMode, data)
