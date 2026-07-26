"""Generated from Smithy shape ``com.amazonaws.geoplaces#BusinessChainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.business_chain

BusinessChainList: TypeAlias = list[
    "capo_geo_places.types.business_chain.BusinessChain"
]


# --- restJson1 ser/de ---
def serialize_json(value: BusinessChainList) -> list:
    import capo_geo_places.types.business_chain

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.business_chain.serialize_json(item))
    return out


def deserialize_json(data: list) -> BusinessChainList:
    import capo_geo_places.types.business_chain

    out: BusinessChainList = []
    for item in data:
        out.append(capo_geo_places.types.business_chain.deserialize_json(item))
    return out
