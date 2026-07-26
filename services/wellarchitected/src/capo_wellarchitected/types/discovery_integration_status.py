"""Generated from Smithy shape ``com.amazonaws.wellarchitected#DiscoveryIntegrationStatus``."""

from typing import Literal, TypeAlias, cast

DiscoveryIntegrationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveryIntegrationStatus) -> str:
    return value


def deserialize_json(data: str) -> DiscoveryIntegrationStatus:
    return cast(DiscoveryIntegrationStatus, data)
