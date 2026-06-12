"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveryModification``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

DiscoveryModification: TypeAlias = Literal[
    "DISCOVERED",
    "UPDATED",
    "NO_CHANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISCOVERED",
        "UPDATED",
        "NO_CHANGE",
    )
)


def serialize_json(value: DiscoveryModification) -> str:
    return value


def deserialize_json(data: str) -> DiscoveryModification:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DiscoveryModification value: {data!r}")
    return cast(DiscoveryModification, data)
