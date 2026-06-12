"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListResourceCatalogsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.resource_catalog_name
    import aws_sdk_sagemaker.types.resource_catalog_sort_by
    import aws_sdk_sagemaker.types.resource_catalog_sort_order
    import aws_sdk_sagemaker.types.timestamp


class ListResourceCatalogsRequest(TypedDict):
    name_contains: NotRequired[
        "aws_sdk_sagemaker.types.resource_catalog_name.ResourceCatalogName"
    ]
    """<p> A string that partially matches one or more <code>ResourceCatalog</code>s names. Filters <code>ResourceCatalog</code> by name. </p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p> Use this parameter to search for <code>ResourceCatalog</code>s created after a specific date and time. </p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p> Use this parameter to search for <code>ResourceCatalog</code>s created before a specific date and time. </p>"""
    sort_order: NotRequired[
        "aws_sdk_sagemaker.types.resource_catalog_sort_order.ResourceCatalogSortOrder"
    ]
    """<p> The order in which the resource catalogs are listed. </p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.resource_catalog_sort_by.ResourceCatalogSortBy"
    ]
    """<p> The value on which the resource catalog list is sorted. </p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p> The maximum number of results returned by <code>ListResourceCatalogs</code>. </p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p> A token to resume pagination of <code>ListResourceCatalogs</code> results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceCatalogsRequest) -> dict:
    out: dict = {}
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.resource_catalog_sort_order

        out["SortOrder"] = (
            aws_sdk_sagemaker.types.resource_catalog_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.resource_catalog_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.resource_catalog_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceCatalogsRequest:
    out: ListResourceCatalogsRequest = {}  # type: ignore[typeddict-item]
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.resource_catalog_sort_order

        out["sort_order"] = (
            aws_sdk_sagemaker.types.resource_catalog_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.resource_catalog_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.resource_catalog_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
