"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListHubContentVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.document_schema_version
    import aws_sdk_sagemaker.types.hub_content_name
    import aws_sdk_sagemaker.types.hub_content_sort_by
    import aws_sdk_sagemaker.types.hub_content_type
    import aws_sdk_sagemaker.types.hub_content_version
    import aws_sdk_sagemaker.types.hub_name_or_arn
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.timestamp


class ListHubContentVersionsRequest(TypedDict, closed=True):
    hub_name: NotRequired["aws_sdk_sagemaker.types.hub_name_or_arn.HubNameOrArn"]
    """<p>The name of the hub to list the content versions of.</p>"""
    hub_content_type: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_type.HubContentType"
    ]
    """<p>The type of hub content to list versions of.</p>"""
    hub_content_name: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_name.HubContentName"
    ]
    """<p>The name of the hub content.</p>"""
    min_version: NotRequired[
        "aws_sdk_sagemaker.types.hub_content_version.HubContentVersion"
    ]
    """<p>The lower bound of the hub content versions to list.</p>"""
    max_schema_version: NotRequired[
        "aws_sdk_sagemaker.types.document_schema_version.DocumentSchemaVersion"
    ]
    """<p>The upper bound of the hub content schema version.</p>"""
    creation_time_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Only list hub content versions that were created before the time specified.</p>"""
    creation_time_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Only list hub content versions that were created after the time specified.</p>"""
    sort_by: NotRequired["aws_sdk_sagemaker.types.hub_content_sort_by.HubContentSortBy"]
    """<p>Sort hub content versions by either name or creation time.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>Sort hub content versions by ascending or descending order.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of hub content versions to list.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response to a previous <code>ListHubContentVersions</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of hub content versions, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHubContentVersionsRequest) -> dict:
    out: dict = {}
    if "hub_name" in value:
        out["HubName"] = value["hub_name"]
    if "hub_content_type" in value:
        import aws_sdk_sagemaker.types.hub_content_type

        out["HubContentType"] = (
            aws_sdk_sagemaker.types.hub_content_type.serialize_aws_json_1_1(
                value["hub_content_type"]
            )
        )
    if "hub_content_name" in value:
        out["HubContentName"] = value["hub_content_name"]
    if "min_version" in value:
        out["MinVersion"] = value["min_version"]
    if "max_schema_version" in value:
        out["MaxSchemaVersion"] = value["max_schema_version"]
    if "creation_time_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "creation_time_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.hub_content_sort_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.hub_content_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHubContentVersionsRequest:
    out: ListHubContentVersionsRequest = {}  # type: ignore[typeddict-item]
    if "HubName" in data:
        out["hub_name"] = data["HubName"]
    if "HubContentType" in data:
        import aws_sdk_sagemaker.types.hub_content_type

        out["hub_content_type"] = (
            aws_sdk_sagemaker.types.hub_content_type.deserialize_aws_json_1_1(
                data["HubContentType"]
            )
        )
    if "HubContentName" in data:
        out["hub_content_name"] = data["HubContentName"]
    if "MinVersion" in data:
        out["min_version"] = data["MinVersion"]
    if "MaxSchemaVersion" in data:
        out["max_schema_version"] = data["MaxSchemaVersion"]
    if "CreationTimeBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if "CreationTimeAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.hub_content_sort_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.hub_content_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
