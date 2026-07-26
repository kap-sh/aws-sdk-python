"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingFacetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.listing_facet

ListingFacetList: TypeAlias = list[
    "capo_marketplace_discovery.types.listing_facet.ListingFacet"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingFacetList) -> list:
    import capo_marketplace_discovery.types.listing_facet

    out: list = []
    for item in value:
        out.append(capo_marketplace_discovery.types.listing_facet.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListingFacetList:
    import capo_marketplace_discovery.types.listing_facet

    out: ListingFacetList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.listing_facet.deserialize_json(item)
        )
    return out
