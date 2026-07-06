"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.search_filter_type
    import aws_sdk_marketplace_discovery.types.search_filter_value_list


class SearchFilter(TypedDict, closed=True):
    filter_type: (
        "aws_sdk_marketplace_discovery.types.search_filter_type.SearchFilterType"
    )
    """<p>The type of filter to apply.</p>"""
    filter_values: "aws_sdk_marketplace_discovery.types.search_filter_value_list.SearchFilterValueList"
    """<p>The values to filter by. Term filters accept multiple values (OR logic). Range filters (MIN/MAX_AVERAGE_CUSTOMER_RATING) accept a single value between 0.0 and 5.0.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilter) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.search_filter_type

    out["filterType"] = (
        aws_sdk_marketplace_discovery.types.search_filter_type.serialize_json(
            value["filter_type"]
        )
    )
    import aws_sdk_marketplace_discovery.types.search_filter_value_list

    out["filterValues"] = (
        aws_sdk_marketplace_discovery.types.search_filter_value_list.serialize_json(
            value["filter_values"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchFilter:
    out: SearchFilter = {}  # type: ignore[typeddict-item]
    if "filterType" in data:
        import aws_sdk_marketplace_discovery.types.search_filter_type

        out["filter_type"] = (
            aws_sdk_marketplace_discovery.types.search_filter_type.deserialize_json(
                data["filterType"]
            )
        )
    else:
        raise DeserializationError("SearchFilter.filter_type required")
    if "filterValues" in data:
        import aws_sdk_marketplace_discovery.types.search_filter_value_list

        out["filter_values"] = (
            aws_sdk_marketplace_discovery.types.search_filter_value_list.deserialize_json(
                data["filterValues"]
            )
        )
    else:
        raise DeserializationError("SearchFilter.filter_values required")
    return out
