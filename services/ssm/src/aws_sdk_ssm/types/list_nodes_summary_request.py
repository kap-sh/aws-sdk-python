"""Generated from Smithy shape ``com.amazonaws.ssm#ListNodesSummaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.max_results
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.node_aggregator_list
    import aws_sdk_ssm.types.node_filter_list
    import aws_sdk_ssm.types.resource_data_sync_name


class ListNodesSummaryRequest(TypedDict):
    sync_name: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    ]
    """<p>The name of the Amazon Web Services managed resource data sync to retrieve information about.</p> <p>For cross-account/cross-Region configurations, this parameter is required, and the name of the supported resource data sync is <code>AWS-QuickSetup-ManagedNode</code>.</p> <p>For single account/single-Region configurations, the parameter is not required.</p>"""
    filters: NotRequired["aws_sdk_ssm.types.node_filter_list.NodeFilterList"]
    """<p>One or more filters. Use a filter to generate a summary that matches your specified filter criteria.</p>"""
    aggregators: "aws_sdk_ssm.types.node_aggregator_list.NodeAggregatorList"
    """<p>Specify one or more aggregators to return a count of managed nodes that match that expression. For example, a count of managed nodes by operating system.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.) The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNodesSummaryRequest) -> dict:
    out: dict = {}
    if "sync_name" in value:
        out["SyncName"] = value["sync_name"]
    if "filters" in value:
        import aws_sdk_ssm.types.node_filter_list

        out["Filters"] = aws_sdk_ssm.types.node_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    import aws_sdk_ssm.types.node_aggregator_list

    out["Aggregators"] = aws_sdk_ssm.types.node_aggregator_list.serialize_aws_json_1_1(
        value["aggregators"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNodesSummaryRequest:
    out: ListNodesSummaryRequest = {}  # type: ignore[typeddict-item]
    if "SyncName" in data:
        out["sync_name"] = data["SyncName"]
    if "Filters" in data:
        import aws_sdk_ssm.types.node_filter_list

        out["filters"] = aws_sdk_ssm.types.node_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "Aggregators" in data:
        import aws_sdk_ssm.types.node_aggregator_list

        out["aggregators"] = (
            aws_sdk_ssm.types.node_aggregator_list.deserialize_aws_json_1_1(
                data["Aggregators"]
            )
        )
    else:
        raise DeserializationError("ListNodesSummaryRequest.aggregators required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
