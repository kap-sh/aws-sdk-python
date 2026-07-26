"""Generated from Smithy shape ``com.amazonaws.outposts#SupportedUplinkGbpsListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.supported_uplink_gbps

SupportedUplinkGbpsListDefinition: TypeAlias = list[
    "capo_outposts.types.supported_uplink_gbps.SupportedUplinkGbps"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedUplinkGbpsListDefinition) -> list:
    return list(value)


def deserialize_json(data: list) -> SupportedUplinkGbpsListDefinition:
    return list(data)
