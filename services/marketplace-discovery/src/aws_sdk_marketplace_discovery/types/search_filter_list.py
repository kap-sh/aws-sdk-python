"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.search_filter

SearchFilterList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.search_filter.SearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilterList) -> list:
    import aws_sdk_marketplace_discovery.types.search_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.search_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchFilterList:
    import aws_sdk_marketplace_discovery.types.search_filter

    out: SearchFilterList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.search_filter.deserialize_json(item)
        )
    return out
