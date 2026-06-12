"""Generated from Smithy shape ``com.amazonaws.ssm#GetOpsSummaryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.max_results
    import aws_sdk_ssm.types.next_token
    import aws_sdk_ssm.types.ops_aggregator_list
    import aws_sdk_ssm.types.ops_filter_list
    import aws_sdk_ssm.types.ops_result_attribute_list
    import aws_sdk_ssm.types.resource_data_sync_name


class GetOpsSummaryRequest(TypedDict):
    sync_name: NotRequired[
        "aws_sdk_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    ]
    """<p>Specify the name of a resource data sync to get.</p>"""
    filters: NotRequired["aws_sdk_ssm.types.ops_filter_list.OpsFilterList"]
    """<p>Optional filters used to scope down the returned OpsData. </p>"""
    aggregators: NotRequired["aws_sdk_ssm.types.ops_aggregator_list.OpsAggregatorList"]
    """<p>Optional aggregators that return counts of OpsData based on one or more expressions.</p>"""
    result_attributes: NotRequired[
        "aws_sdk_ssm.types.ops_result_attribute_list.OpsResultAttributeList"
    ]
    """<p>The OpsData data type to return.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""
    max_results: NotRequired["aws_sdk_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpsSummaryRequest) -> dict:
    out: dict = {}
    if "sync_name" in value:
        out["SyncName"] = value["sync_name"]
    if "filters" in value:
        import aws_sdk_ssm.types.ops_filter_list

        out["Filters"] = aws_sdk_ssm.types.ops_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "aggregators" in value:
        import aws_sdk_ssm.types.ops_aggregator_list

        out["Aggregators"] = (
            aws_sdk_ssm.types.ops_aggregator_list.serialize_aws_json_1_1(
                value["aggregators"]
            )
        )
    if "result_attributes" in value:
        import aws_sdk_ssm.types.ops_result_attribute_list

        out["ResultAttributes"] = (
            aws_sdk_ssm.types.ops_result_attribute_list.serialize_aws_json_1_1(
                value["result_attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpsSummaryRequest:
    out: GetOpsSummaryRequest = {}  # type: ignore[typeddict-item]
    if "SyncName" in data:
        out["sync_name"] = data["SyncName"]
    if "Filters" in data:
        import aws_sdk_ssm.types.ops_filter_list

        out["filters"] = aws_sdk_ssm.types.ops_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "Aggregators" in data:
        import aws_sdk_ssm.types.ops_aggregator_list

        out["aggregators"] = (
            aws_sdk_ssm.types.ops_aggregator_list.deserialize_aws_json_1_1(
                data["Aggregators"]
            )
        )
    if "ResultAttributes" in data:
        import aws_sdk_ssm.types.ops_result_attribute_list

        out["result_attributes"] = (
            aws_sdk_ssm.types.ops_result_attribute_list.deserialize_aws_json_1_1(
                data["ResultAttributes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
