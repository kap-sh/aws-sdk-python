"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListResourceCatalogsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.resource_catalog_name
    import capo_sagemaker.types.resource_catalog_sort_by
    import capo_sagemaker.types.resource_catalog_sort_order
    import capo_sagemaker.types.timestamp


class ListResourceCatalogsRequest(TypedDict, closed=True):
    name_contains: NotRequired[
        "capo_sagemaker.types.resource_catalog_name.ResourceCatalogName"
    ]
    """<p> A string that partially matches one or more <code>ResourceCatalog</code>s names. Filters <code>ResourceCatalog</code> by name. </p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p> Use this parameter to search for <code>ResourceCatalog</code>s created after a specific date and time. </p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p> Use this parameter to search for <code>ResourceCatalog</code>s created before a specific date and time. </p>"""
    sort_order: NotRequired[
        "capo_sagemaker.types.resource_catalog_sort_order.ResourceCatalogSortOrder"
    ]
    """<p> The order in which the resource catalogs are listed. </p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.resource_catalog_sort_by.ResourceCatalogSortBy"
    ]
    """<p> The value on which the resource catalog list is sorted. </p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p> The maximum number of results returned by <code>ListResourceCatalogs</code>. </p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p> A token to resume pagination of <code>ListResourceCatalogs</code> results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceCatalogsRequest) -> dict:
    out: dict = {}
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "creation_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.resource_catalog_sort_order

        out["SortOrder"] = (
            capo_sagemaker.types.resource_catalog_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "sort_by" in value:
        import capo_sagemaker.types.resource_catalog_sort_by

        out["SortBy"] = (
            capo_sagemaker.types.resource_catalog_sort_by.serialize_aws_json_1_1(
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
        import capo_sagemaker.types.timestamp

        out["creation_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "CreationTimeBefore" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.resource_catalog_sort_order

        out["sort_order"] = (
            capo_sagemaker.types.resource_catalog_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    if "SortBy" in data:
        import capo_sagemaker.types.resource_catalog_sort_by

        out["sort_by"] = (
            capo_sagemaker.types.resource_catalog_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
