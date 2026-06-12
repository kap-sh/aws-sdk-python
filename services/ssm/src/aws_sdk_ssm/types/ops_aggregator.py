"""Generated from Smithy shape ``com.amazonaws.ssm#OpsAggregator``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_aggregator_list
    import aws_sdk_ssm.types.ops_aggregator_type
    import aws_sdk_ssm.types.ops_aggregator_value_map
    import aws_sdk_ssm.types.ops_data_attribute_name
    import aws_sdk_ssm.types.ops_data_type_name
    import aws_sdk_ssm.types.ops_filter_list


class OpsAggregator(TypedDict):
    aggregator_type: NotRequired[
        "aws_sdk_ssm.types.ops_aggregator_type.OpsAggregatorType"
    ]
    """<p>Either a <code>Range</code> or <code>Count</code> aggregator for limiting an OpsData summary.</p>"""
    type_name: NotRequired["aws_sdk_ssm.types.ops_data_type_name.OpsDataTypeName"]
    """<p>The data type name to use for viewing counts of OpsData.</p>"""
    attribute_name: NotRequired[
        "aws_sdk_ssm.types.ops_data_attribute_name.OpsDataAttributeName"
    ]
    """<p>The name of an OpsData attribute on which to limit the count of OpsData.</p>"""
    values: NotRequired[
        "aws_sdk_ssm.types.ops_aggregator_value_map.OpsAggregatorValueMap"
    ]
    """<p>The aggregator value.</p>"""
    filters: NotRequired["aws_sdk_ssm.types.ops_filter_list.OpsFilterList"]
    """<p>The aggregator filters.</p>"""
    aggregators: NotRequired["aws_sdk_ssm.types.ops_aggregator_list.OpsAggregatorList"]
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
        import aws_sdk_ssm.types.ops_aggregator_value_map

        out["Values"] = (
            aws_sdk_ssm.types.ops_aggregator_value_map.serialize_aws_json_1_1(
                value["values"]
            )
        )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsAggregator:
    out: OpsAggregator = {}  # type: ignore[typeddict-item]
    if "AggregatorType" in data:
        out["aggregator_type"] = data["AggregatorType"]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    if "Values" in data:
        import aws_sdk_ssm.types.ops_aggregator_value_map

        out["values"] = (
            aws_sdk_ssm.types.ops_aggregator_value_map.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
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
    return out
