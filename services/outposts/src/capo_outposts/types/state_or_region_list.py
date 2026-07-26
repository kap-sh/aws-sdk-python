"""Generated from Smithy shape ``com.amazonaws.outposts#StateOrRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.state_or_region

StateOrRegionList: TypeAlias = list["capo_outposts.types.state_or_region.StateOrRegion"]


# --- restJson1 ser/de ---
def serialize_json(value: StateOrRegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> StateOrRegionList:
    return list(data)
