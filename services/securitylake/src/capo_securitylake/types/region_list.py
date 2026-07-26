"""Generated from Smithy shape ``com.amazonaws.securitylake#RegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securitylake.types.region

RegionList: TypeAlias = list["capo_securitylake.types.region.Region"]


# --- restJson1 ser/de ---
def serialize_json(value: RegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegionList:
    return list(data)
