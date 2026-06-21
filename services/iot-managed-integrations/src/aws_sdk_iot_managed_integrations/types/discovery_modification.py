"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveryModification``."""

from typing import Literal, TypeAlias, cast

DiscoveryModification: TypeAlias = Literal[
    "DISCOVERED",
    "UPDATED",
    "NO_CHANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveryModification) -> str:
    return value


def deserialize_json(data: str) -> DiscoveryModification:
    return cast(DiscoveryModification, data)
