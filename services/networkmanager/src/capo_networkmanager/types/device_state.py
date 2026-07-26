"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeviceState``."""

from typing import Literal, TypeAlias, cast

DeviceState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceState) -> str:
    return value


def deserialize_json(data: str) -> DeviceState:
    return cast(DeviceState, data)
