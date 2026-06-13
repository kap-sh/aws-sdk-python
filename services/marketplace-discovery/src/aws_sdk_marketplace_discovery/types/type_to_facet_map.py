"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#TypeToFacetMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.listing_facet_list
    import aws_sdk_marketplace_discovery.types.search_facet_type

TypeToFacetMap: TypeAlias = dict[
    "aws_sdk_marketplace_discovery.types.search_facet_type.SearchFacetType",
    "aws_sdk_marketplace_discovery.types.listing_facet_list.ListingFacetList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TypeToFacetMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_marketplace_discovery.types.listing_facet_list
        import aws_sdk_marketplace_discovery.types.search_facet_type

        out[
            aws_sdk_marketplace_discovery.types.search_facet_type.serialize_json(key)
        ] = aws_sdk_marketplace_discovery.types.listing_facet_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> TypeToFacetMap:
    out: TypeToFacetMap = {}
    for key, value in data.items():
        import aws_sdk_marketplace_discovery.types.listing_facet_list
        import aws_sdk_marketplace_discovery.types.search_facet_type

        out[
            aws_sdk_marketplace_discovery.types.search_facet_type.deserialize_json(key)
        ] = aws_sdk_marketplace_discovery.types.listing_facet_list.deserialize_json(
            value
        )
    return out
