"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DependencyDiscoveryStatus``."""

from typing import Literal, TypeAlias, cast

DependencyDiscoveryStatus: TypeAlias = Literal[
    "ENABLED",
    "INITIALIZING",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DependencyDiscoveryStatus) -> str:
    return value


def deserialize_json(data: str) -> DependencyDiscoveryStatus:
    return cast(DependencyDiscoveryStatus, data)
