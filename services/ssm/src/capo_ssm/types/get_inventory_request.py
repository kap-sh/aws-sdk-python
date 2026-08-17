"""Generated from Smithy shape ``com.amazonaws.ssm#GetInventoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.inventory_aggregator_list
    import capo_ssm.types.inventory_filter_list
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token
    import capo_ssm.types.result_attribute_list


class GetInventoryRequest(TypedDict, closed=True):
    filters: NotRequired["capo_ssm.types.inventory_filter_list.InventoryFilterList"]
    """<p>One or more filters. Use a filter to return a more specific list of results.</p>"""
    aggregators: NotRequired[
        "capo_ssm.types.inventory_aggregator_list.InventoryAggregatorList"
    ]
    """<p>Returns counts of inventory types based on one or more expressions. For example, if you aggregate by using an expression that uses the <code>AWS:InstanceInformation.PlatformType</code> type, you can see a count of how many Windows and Linux managed nodes exist in your inventoried fleet.</p>"""
    result_attributes: NotRequired[
        "capo_ssm.types.result_attribute_list.ResultAttributeList"
    ]
    """<p>The list of inventory item types to return.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInventoryRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_ssm.types.inventory_filter_list

        out["Filters"] = capo_ssm.types.inventory_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    if "aggregators" in value:
        import capo_ssm.types.inventory_aggregator_list

        out["Aggregators"] = (
            capo_ssm.types.inventory_aggregator_list.serialize_aws_json_1_1(
                value["aggregators"]
            )
        )
    if "result_attributes" in value:
        import capo_ssm.types.result_attribute_list

        out["ResultAttributes"] = (
            capo_ssm.types.result_attribute_list.serialize_aws_json_1_1(
                value["result_attributes"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInventoryRequest:
    out: GetInventoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_ssm.types.inventory_filter_list

        out["filters"] = capo_ssm.types.inventory_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("Aggregators") is not None:
        import capo_ssm.types.inventory_aggregator_list

        out["aggregators"] = (
            capo_ssm.types.inventory_aggregator_list.deserialize_aws_json_1_1(
                data["Aggregators"]
            )
        )
    if data.get("ResultAttributes") is not None:
        import capo_ssm.types.result_attribute_list

        out["result_attributes"] = (
            capo_ssm.types.result_attribute_list.deserialize_aws_json_1_1(
                data["ResultAttributes"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
