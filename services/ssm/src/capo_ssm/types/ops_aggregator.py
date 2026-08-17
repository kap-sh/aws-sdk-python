"""Generated from Smithy shape ``com.amazonaws.ssm#OpsAggregator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_aggregator_list
    import capo_ssm.types.ops_aggregator_type
    import capo_ssm.types.ops_aggregator_value_map
    import capo_ssm.types.ops_data_attribute_name
    import capo_ssm.types.ops_data_type_name
    import capo_ssm.types.ops_filter_list


class OpsAggregator(TypedDict, closed=True):
    aggregator_type: NotRequired["capo_ssm.types.ops_aggregator_type.OpsAggregatorType"]
    """<p>Either a <code>Range</code> or <code>Count</code> aggregator for limiting an OpsData summary.</p>"""
    type_name: NotRequired["capo_ssm.types.ops_data_type_name.OpsDataTypeName"]
    """<p>The data type name to use for viewing counts of OpsData.</p>"""
    attribute_name: NotRequired[
        "capo_ssm.types.ops_data_attribute_name.OpsDataAttributeName"
    ]
    """<p>The name of an OpsData attribute on which to limit the count of OpsData.</p>"""
    values: NotRequired["capo_ssm.types.ops_aggregator_value_map.OpsAggregatorValueMap"]
    """<p>The aggregator value.</p>"""
    filters: NotRequired["capo_ssm.types.ops_filter_list.OpsFilterList"]
    """<p>The aggregator filters.</p>"""
    aggregators: NotRequired["capo_ssm.types.ops_aggregator_list.OpsAggregatorList"]
    """<p>A nested aggregator for viewing counts of OpsData.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsAggregator) -> dict:
    out: dict = {}
    if "aggregator_type" in value:
        out["AggregatorType"] = value["aggregator_type"]
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    if "values" in value:
        import capo_ssm.types.ops_aggregator_value_map

        out["Values"] = capo_ssm.types.ops_aggregator_value_map.serialize_aws_json_1_1(
            value["values"]
        )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsAggregator:
    out: OpsAggregator = {}  # type: ignore[typeddict-item]
    if data.get("AggregatorType") is not None:
        out["aggregator_type"] = data["AggregatorType"]
    if data.get("TypeName") is not None:
        out["type_name"] = data["TypeName"]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    if data.get("Values") is not None:
        import capo_ssm.types.ops_aggregator_value_map

        out["values"] = (
            capo_ssm.types.ops_aggregator_value_map.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
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
    return out
