"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingFacetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.listing_facet

ListingFacetList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.listing_facet.ListingFacet"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingFacetList) -> list:
    import aws_sdk_marketplace_discovery.types.listing_facet

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.listing_facet.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListingFacetList:
    import aws_sdk_marketplace_discovery.types.listing_facet

    out: ListingFacetList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.listing_facet.deserialize_json(item)
        )
    return out
