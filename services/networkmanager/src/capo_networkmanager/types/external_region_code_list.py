"""Generated from Smithy shape ``com.amazonaws.networkmanager#ExternalRegionCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.external_region_code

ExternalRegionCodeList: TypeAlias = list[
    "capo_networkmanager.types.external_region_code.ExternalRegionCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExternalRegionCodeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ExternalRegionCodeList:
    return list(data)
