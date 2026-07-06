"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SearchProductsAsAdminInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.page_size
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.product_source
    import aws_sdk_service_catalog.types.product_view_filters
    import aws_sdk_service_catalog.types.product_view_sort_by
    import aws_sdk_service_catalog.types.sort_order


class SearchProductsAsAdminInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    portfolio_id: NotRequired["aws_sdk_service_catalog.types.id.Id"]
    """<p>The portfolio identifier.</p>"""
    filters: NotRequired[
        "aws_sdk_service_catalog.types.product_view_filters.ProductViewFilters"
    ]
    """<p>The search filters. If no search filters are specified, the output includes all products to which the administrator has access.</p>"""
    sort_by: NotRequired[
        "aws_sdk_service_catalog.types.product_view_sort_by.ProductViewSortBy"
    ]
    """<p>The sort field. If no value is specified, the results are not sorted.</p>"""
    sort_order: NotRequired["aws_sdk_service_catalog.types.sort_order.SortOrder"]
    """<p>The sort order. If no value is specified, the results are not sorted.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""
    page_size: "aws_sdk_service_catalog.types.page_size.PageSize"
    """<p>The maximum number of items to return with this call.</p>"""
    product_source: NotRequired[
        "aws_sdk_service_catalog.types.product_source.ProductSource"
    ]
    """<p>Access level of the source of the product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchProductsAsAdminInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "portfolio_id" in value:
        out["PortfolioId"] = value["portfolio_id"]
    if "filters" in value:
        import aws_sdk_service_catalog.types.product_view_filters

        out["Filters"] = (
            aws_sdk_service_catalog.types.product_view_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
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
    out["PageSize"] = value.get("page_size", 0)
    if "product_source" in value:
        import aws_sdk_service_catalog.types.product_source

        out["ProductSource"] = (
            aws_sdk_service_catalog.types.product_source.serialize_aws_json_1_1(
                value["product_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchProductsAsAdminInput:
    out: SearchProductsAsAdminInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "PortfolioId" in data:
        out["portfolio_id"] = data["PortfolioId"]
    if "Filters" in data:
        import aws_sdk_service_catalog.types.product_view_filters

        out["filters"] = (
            aws_sdk_service_catalog.types.product_view_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
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
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "ProductSource" in data:
        import aws_sdk_service_catalog.types.product_source

        out["product_source"] = (
            aws_sdk_service_catalog.types.product_source.deserialize_aws_json_1_1(
                data["ProductSource"]
            )
        )
    return out
