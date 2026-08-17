"""Generated from Smithy shape ``com.amazonaws.ssm#GetOpsSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token
    import capo_ssm.types.ops_aggregator_list
    import capo_ssm.types.ops_filter_list
    import capo_ssm.types.ops_result_attribute_list
    import capo_ssm.types.resource_data_sync_name


class GetOpsSummaryRequest(TypedDict, closed=True):
    sync_name: NotRequired[
        "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    ]
    """<p>Specify the name of a resource data sync to get.</p>"""
    filters: NotRequired["capo_ssm.types.ops_filter_list.OpsFilterList"]
    """<p>Optional filters used to scope down the returned OpsData. </p>"""
    aggregators: NotRequired["capo_ssm.types.ops_aggregator_list.OpsAggregatorList"]
    """<p>Optional aggregators that return counts of OpsData based on one or more expressions.</p>"""
    result_attributes: NotRequired[
        "capo_ssm.types.ops_result_attribute_list.OpsResultAttributeList"
    ]
    """<p>The OpsData data type to return.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results. </p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpsSummaryRequest) -> dict:
    out: dict = {}
    if "sync_name" in value:
        out["SyncName"] = value["sync_name"]
    if "filters" in value:
        import capo_ssm.types.ops_filter_list

        out["Filters"] = capo_ssm.types.ops_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "aggregators" in value:
        import capo_ssm.types.ops_aggregator_list

        out["Aggregators"] = capo_ssm.types.ops_aggregator_list.serialize_aws_json_1_1(
            value["aggregators"]
        )
    if "result_attributes" in value:
        import capo_ssm.types.ops_result_attribute_list

        out["ResultAttributes"] = (
            capo_ssm.types.ops_result_attribute_list.serialize_aws_json_1_1(
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
    if data.get("SyncName") is not None:
        out["sync_name"] = data["SyncName"]
    if data.get("Filters") is not None:
        import capo_ssm.types.ops_filter_list

        out["filters"] = capo_ssm.types.ops_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("Aggregators") is not None:
        import capo_ssm.types.ops_aggregator_list

        out["aggregators"] = (
            capo_ssm.types.ops_aggregator_list.deserialize_aws_json_1_1(
                data["Aggregators"]
            )
        )
    if data.get("ResultAttributes") is not None:
        import capo_ssm.types.ops_result_attribute_list

        out["result_attributes"] = (
            capo_ssm.types.ops_result_attribute_list.deserialize_aws_json_1_1(
                data["ResultAttributes"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
