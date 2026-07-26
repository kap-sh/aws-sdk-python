"""Generated from Smithy shape ``com.amazonaws.controlcatalog#DeployableRegions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controlcatalog.types.region_code

DeployableRegions: TypeAlias = list["capo_controlcatalog.types.region_code.RegionCode"]


# --- restJson1 ser/de ---
def serialize_json(value: DeployableRegions) -> list:
    return list(value)


def deserialize_json(data: list) -> DeployableRegions:
    return list(data)
