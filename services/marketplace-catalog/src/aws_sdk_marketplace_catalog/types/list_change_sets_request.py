"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ListChangeSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.catalog
    import aws_sdk_marketplace_catalog.types.filter_list
    import aws_sdk_marketplace_catalog.types.list_change_sets_max_result_integer
    import aws_sdk_marketplace_catalog.types.next_token
    import aws_sdk_marketplace_catalog.types.sort


class ListChangeSetsRequest(TypedDict, closed=True):
    catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog"
    """<p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>"""
    filter_list: NotRequired["aws_sdk_marketplace_catalog.types.filter_list.FilterList"]
    """<p>An array of filter objects.</p>"""
    sort: NotRequired["aws_sdk_marketplace_catalog.types.sort.Sort"]
    """<p>An object that contains two attributes, <code>SortBy</code> and <code>SortOrder</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_marketplace_catalog.types.list_change_sets_max_result_integer.ListChangeSetsMaxResultInteger"
    ]
    """<p>The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results. By default, this value is 20.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_catalog.types.next_token.NextToken"]
    """<p>The token value retrieved from a previous call to access the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListChangeSetsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "filter_list" in value:
        import aws_sdk_marketplace_catalog.types.filter_list

        out["FilterList"] = (
            aws_sdk_marketplace_catalog.types.filter_list.serialize_json(
                value["filter_list"]
            )
        )
    if "sort" in value:
        import aws_sdk_marketplace_catalog.types.sort

        out["Sort"] = aws_sdk_marketplace_catalog.types.sort.serialize_json(
            value["sort"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListChangeSetsRequest:
    out: ListChangeSetsRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListChangeSetsRequest.catalog required")
    if "FilterList" in data:
        import aws_sdk_marketplace_catalog.types.filter_list

        out["filter_list"] = (
            aws_sdk_marketplace_catalog.types.filter_list.deserialize_json(
                data["FilterList"]
            )
        )
    if "Sort" in data:
        import aws_sdk_marketplace_catalog.types.sort

        out["sort"] = aws_sdk_marketplace_catalog.types.sort.deserialize_json(
            data["Sort"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
