"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchFacetsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.next_token
    import aws_sdk_marketplace_discovery.types.non_negative_count
    import aws_sdk_marketplace_discovery.types.type_to_facet_map


class SearchFacetsOutput(TypedDict):
    total_results: (
        "aws_sdk_marketplace_discovery.types.non_negative_count.NonNegativeCount"
    )
    """<p>The total number of listings matching the search criteria.</p>"""
    listing_facets: (
        "aws_sdk_marketplace_discovery.types.type_to_facet_map.TypeToFacetMap"
    )
    """<p>A map of facet types to their corresponding facet values. Each facet value includes a display name, internal value, and count of matching listings.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_discovery.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFacetsOutput) -> dict:
    out: dict = {}
    out["totalResults"] = value["total_results"]
    import aws_sdk_marketplace_discovery.types.type_to_facet_map

    out["listingFacets"] = (
        aws_sdk_marketplace_discovery.types.type_to_facet_map.serialize_json(
            value["listing_facets"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchFacetsOutput:
    out: SearchFacetsOutput = {}  # type: ignore[typeddict-item]
    if "totalResults" in data:
        out["total_results"] = data["totalResults"]
    else:
        raise DeserializationError("SearchFacetsOutput.total_results required")
    if "listingFacets" in data:
        import aws_sdk_marketplace_discovery.types.type_to_facet_map

        out["listing_facets"] = (
            aws_sdk_marketplace_discovery.types.type_to_facet_map.deserialize_json(
                data["listingFacets"]
            )
        )
    else:
        raise DeserializationError("SearchFacetsOutput.listing_facets required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
