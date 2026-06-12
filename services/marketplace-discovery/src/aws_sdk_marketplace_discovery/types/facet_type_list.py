"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FacetTypeList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.search_facet_type

FacetTypeList: TypeAlias = list["aws_sdk_marketplace_discovery.types.search_facet_type.SearchFacetType"]


# --- restJson1 ser/de ---
def serialize_json(value: FacetTypeList) -> list:
    import aws_sdk_marketplace_discovery.types.search_facet_type
    out: list = []
    for item in value:
        out.append(aws_sdk_marketplace_discovery.types.search_facet_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> FacetTypeList:
    import aws_sdk_marketplace_discovery.types.search_facet_type
    out: FacetTypeList = []
    for item in data:
        out.append(aws_sdk_marketplace_discovery.types.search_facet_type.deserialize_json(item))
    return out