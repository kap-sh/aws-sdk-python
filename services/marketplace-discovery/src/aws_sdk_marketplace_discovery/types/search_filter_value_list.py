"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.search_filter_value

SearchFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.search_filter_value.SearchFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> SearchFilterValueList:
    return list(data)
