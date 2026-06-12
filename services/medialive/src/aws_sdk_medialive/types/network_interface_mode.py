"""Generated from Smithy shape ``com.amazonaws.medialive#NetworkInterfaceMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Used in NodeInterfaceMapping and NodeInterfaceMappingCreateRequest"""
NetworkInterfaceMode: TypeAlias = Literal[
    "NAT",
    "BRIDGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAT",
        "BRIDGE",
    )
)


def serialize_json(value: NetworkInterfaceMode) -> str:
    return value


def deserialize_json(data: str) -> NetworkInterfaceMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NetworkInterfaceMode value: {data!r}")
    return cast(NetworkInterfaceMode, data)
