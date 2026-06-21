"""Generated from Smithy shape ``com.amazonaws.medialive#NetworkInterfaceMode``."""

from typing import Literal, TypeAlias, cast

"""Used in NodeInterfaceMapping and NodeInterfaceMappingCreateRequest"""
NetworkInterfaceMode: TypeAlias = Literal[
    "NAT",
    "BRIDGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterfaceMode) -> str:
    return value


def deserialize_json(data: str) -> NetworkInterfaceMode:
    return cast(NetworkInterfaceMode, data)
