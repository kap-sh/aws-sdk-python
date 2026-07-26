"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListHubContentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.document_schema_version
    import capo_sagemaker.types.hub_content_sort_by
    import capo_sagemaker.types.hub_content_type
    import capo_sagemaker.types.hub_name_or_arn
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.name_contains
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp


class ListHubContentsRequest(TypedDict, closed=True):
    hub_name: NotRequired["capo_sagemaker.types.hub_name_or_arn.HubNameOrArn"]
    """<p>The name of the hub to list the contents of.</p>"""
    hub_content_type: NotRequired[
        "capo_sagemaker.types.hub_content_type.HubContentType"
    ]
    """<p>The type of hub content to list.</p>"""
    name_contains: NotRequired["capo_sagemaker.types.name_contains.NameContains"]
    """<p>Only list hub content if the name contains the specified string.</p>"""
    max_schema_version: NotRequired[
        "capo_sagemaker.types.document_schema_version.DocumentSchemaVersion"
    ]
    """<p>The upper bound of the hub content schema verion.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Only list hub content that was created before the time specified.</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Only list hub content that was created after the time specified.</p>"""
    sort_by: NotRequired["capo_sagemaker.types.hub_content_sort_by.HubContentSortBy"]
    """<p>Sort hub content versions by either name or creation time.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>Sort hubs by ascending or descending order.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum amount of hub content to list.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response to a previous <code>ListHubContents</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of hub content, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHubContentsRequest) -> dict:
    out: dict = {}
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "hub_content_type" in value:
        import capo_sagemaker.types.hub_content_type

        out["HubContentType"] = (
            capo_sagemaker.types.hub_content_type.serialize_aws_json_1_1(
                value["hub_content_type"]
            )
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "max_schema_version" in value:
        out["MaxSchemaVersion"] = value["max_schema_version"]
    if "creation_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "creation_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "sort_by" in value:
        import capo_sagemaker.types.hub_content_sort_by

        out["SortBy"] = capo_sagemaker.types.hub_content_sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHubContentsRequest:
    out: ListHubContentsRequest = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubContentType" in data:
        import capo_sagemaker.types.hub_content_type

        out["hub_content_type"] = (
            capo_sagemaker.types.hub_content_type.deserialize_aws_json_1_1(
                data["HubContentType"]
            )
        )
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "MaxSchemaVersion" in data:
        out["max_schema_version"] = data["MaxSchemaVersion"]
    if "CreationTimeBefore" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "CreationTimeAfter" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "SortBy" in data:
        import capo_sagemaker.types.hub_content_sort_by

        out["sort_by"] = (
            capo_sagemaker.types.hub_content_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
