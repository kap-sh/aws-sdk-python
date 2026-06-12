"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterSchedulerConfigsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_arn
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.scheduler_resource_status
    import aws_sdk_sagemaker.types.sort_cluster_scheduler_config_by
    import aws_sdk_sagemaker.types.sort_order
    import aws_sdk_sagemaker.types.timestamp


class ListClusterSchedulerConfigsRequest(TypedDict):
    created_after: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter for after this creation time. The input for this parameter is a Unix timestamp. To convert a date and time into a Unix timestamp, see <a href=\"https://www.epochconverter.com/\">EpochConverter</a>.</p>"""
    created_before: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter for before this creation time. The input for this parameter is a Unix timestamp. To convert a date and time into a Unix timestamp, see <a href=\"https://www.epochconverter.com/\">EpochConverter</a>.</p>"""
    name_contains: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>Filter for name containing this string.</p>"""
    cluster_arn: NotRequired["aws_sdk_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>Filter for ARN of the cluster.</p>"""
    status: NotRequired[
        "aws_sdk_sagemaker.types.scheduler_resource_status.SchedulerResourceStatus"
    ]
    """<p>Filter for status.</p>"""
    sort_by: NotRequired[
        "aws_sdk_sagemaker.types.sort_cluster_scheduler_config_by.SortClusterSchedulerConfigBy"
    ]
    """<p>Filter for sorting the list by a given value. For example, sort by name, creation time, or status.</p>"""
    sort_order: NotRequired["aws_sdk_sagemaker.types.sort_order.SortOrder"]
    """<p>The order of the list. By default, listed in <code>Descending</code> order according to by <code>SortBy</code>. To change the list order, you can specify <code>SortOrder</code> to be <code>Ascending</code>.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of cluster policies to list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterSchedulerConfigsRequest) -> dict:
    out: dict = {}
    if "created_after" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedAfter"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreatedBefore"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "status" in value:
        import aws_sdk_sagemaker.types.scheduler_resource_status

        out["Status"] = (
            aws_sdk_sagemaker.types.scheduler_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "sort_by" in value:
        import aws_sdk_sagemaker.types.sort_cluster_scheduler_config_by

        out["SortBy"] = (
            aws_sdk_sagemaker.types.sort_cluster_scheduler_config_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import aws_sdk_sagemaker.types.sort_order

        out["SortOrder"] = aws_sdk_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterSchedulerConfigsRequest:
    out: ListClusterSchedulerConfigsRequest = {}  # type: ignore[typeddict-item]
    if "CreatedAfter" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_after"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedAfter"]
            )
        )
    if "CreatedBefore" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["created_before"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreatedBefore"]
            )
        )
    if "NameContains" in data:
        out["name_contains"] = data["NameContains"]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.scheduler_resource_status

        out["status"] = (
            aws_sdk_sagemaker.types.scheduler_resource_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "SortBy" in data:
        import aws_sdk_sagemaker.types.sort_cluster_scheduler_config_by

        out["sort_by"] = (
            aws_sdk_sagemaker.types.sort_cluster_scheduler_config_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_sagemaker.types.sort_order

        out["sort_order"] = aws_sdk_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
