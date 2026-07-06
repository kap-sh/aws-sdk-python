"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SearchProvisionedProductsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.access_level_filter
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.provisioned_product_filters
    import aws_sdk_service_catalog.types.search_provisioned_products_page_size
    import aws_sdk_service_catalog.types.sort_field
    import aws_sdk_service_catalog.types.sort_order


class SearchProvisionedProductsInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    access_level_filter: NotRequired[
        "aws_sdk_service_catalog.types.access_level_filter.AccessLevelFilter"
    ]
    """<p>The access level to use to obtain results. The default is <code>Account</code>.</p>"""
    filters: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_filters.ProvisionedProductFilters"
    ]
    r"""<p>The search filters.</p> <p>When the key is <code>SearchQuery</code>, the searchable fields are <code>arn</code>, <code>createdTime</code>, <code>id</code>, <code>lastRecordId</code>, <code>idempotencyToken</code>, <code>name</code>, <code>physicalId</code>, <code>productId</code>, <code>provisioningArtifactId</code>, <code>type</code>, <code>status</code>, <code>tags</code>, <code>userArn</code>, <code>userArnSession</code>, <code>lastProvisioningRecordId</code>, <code>lastSuccessfulProvisioningRecordId</code>, <code>productName</code>, and <code>provisioningArtifactName</code>.</p> <p>Example: <code>\"SearchQuery\":[\"status:AVAILABLE\"]</code> </p>"""
    sort_by: NotRequired["aws_sdk_service_catalog.types.sort_field.SortField"]
    """<p>The sort field. If no value is specified, the results are not sorted. The valid values are <code>arn</code>, <code>id</code>, <code>name</code>, and <code>lastRecordId</code>.</p>"""
    sort_order: NotRequired["aws_sdk_service_catalog.types.sort_order.SortOrder"]
    """<p>The sort order. If no value is specified, the results are not sorted.</p>"""
    page_size: "aws_sdk_service_catalog.types.search_provisioned_products_page_size.SearchProvisionedProductsPageSize"
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchProvisionedProductsInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "access_level_filter" in value:
        import aws_sdk_service_catalog.types.access_level_filter

        out["AccessLevelFilter"] = (
            aws_sdk_service_catalog.types.access_level_filter.serialize_aws_json_1_1(
                value["access_level_filter"]
            )
        )
    if "filters" in value:
        import aws_sdk_service_catalog.types.provisioned_product_filters

        out["Filters"] = (
            aws_sdk_service_catalog.types.provisioned_product_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "sort_by" in value:
        out["SortBy"] = value["sort_by"]
    if "sort_order" in value:
        import aws_sdk_service_catalog.types.sort_order

        out["SortOrder"] = (
            aws_sdk_service_catalog.types.sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    out["PageSize"] = value.get("page_size", 0)
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchProvisionedProductsInput:
    out: SearchProvisionedProductsInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "AccessLevelFilter" in data:
        import aws_sdk_service_catalog.types.access_level_filter

        out["access_level_filter"] = (
            aws_sdk_service_catalog.types.access_level_filter.deserialize_aws_json_1_1(
                data["AccessLevelFilter"]
            )
        )
    if "Filters" in data:
        import aws_sdk_service_catalog.types.provisioned_product_filters

        out["filters"] = (
            aws_sdk_service_catalog.types.provisioned_product_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "SortBy" in data:
        out["sort_by"] = data["SortBy"]
    if "SortOrder" in data:
        import aws_sdk_service_catalog.types.sort_order

        out["sort_order"] = (
            aws_sdk_service_catalog.types.sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "PageToken" in data:
        out["page_token"] = data["PageToken"]
    return out
