"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SearchProductsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.page_size_max100
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.product_view_filters
    import aws_sdk_service_catalog.types.product_view_sort_by
    import aws_sdk_service_catalog.types.sort_order


class SearchProductsInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    filters: NotRequired[
        "aws_sdk_service_catalog.types.product_view_filters.ProductViewFilters"
    ]
    """<p>The search filters. If no search filters are specified, the output includes all products to which the caller has access.</p>"""
    page_size: "aws_sdk_service_catalog.types.page_size_max100.PageSizeMax100"
    """<p>The maximum number of items to return with this call.</p>"""
    sort_by: NotRequired[
        "aws_sdk_service_catalog.types.product_view_sort_by.ProductViewSortBy"
    ]
    """<p>The sort field. If no value is specified, the results are not sorted.</p>"""
    sort_order: NotRequired["aws_sdk_service_catalog.types.sort_order.SortOrder"]
    """<p>The sort order. If no value is specified, the results are not sorted.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchProductsInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "filters" in value:
        import aws_sdk_service_catalog.types.product_view_filters

        out["Filters"] = (
            aws_sdk_service_catalog.types.product_view_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    out["PageSize"] = value.get("page_size", 0)
    if "sort_by" in value:
        import aws_sdk_service_catalog.types.product_view_sort_by

        out["SortBy"] = (
            aws_sdk_service_catalog.types.product_view_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_service_catalog.types.sort_order

        out["SortOrder"] = (
            aws_sdk_service_catalog.types.sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchProductsInput:
    out: SearchProductsInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "Filters" in data:
        import aws_sdk_service_catalog.types.product_view_filters

        out["filters"] = (
            aws_sdk_service_catalog.types.product_view_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "SortBy" in data:
        import aws_sdk_service_catalog.types.product_view_sort_by

        out["sort_by"] = (
            aws_sdk_service_catalog.types.product_view_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_service_catalog.types.sort_order

        out["sort_order"] = (
            aws_sdk_service_catalog.types.sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "PageToken" in data:
        out["page_token"] = data["PageToken"]
    return out
