"""Generated from Smithy shape ``com.amazonaws.ssm#NodeAggregator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.node_aggregator_list
    import aws_sdk_ssm.types.node_aggregator_type
    import aws_sdk_ssm.types.node_attribute_name
    import aws_sdk_ssm.types.node_type_name


class NodeAggregator(TypedDict, closed=True):
    aggregator_type: "aws_sdk_ssm.types.node_aggregator_type.NodeAggregatorType"
    """<p>The aggregator type for limiting a node summary. Currently, only <code>Count</code> is supported.</p>"""
    type_name: "aws_sdk_ssm.types.node_type_name.NodeTypeName"
    """<p>The data type name to use for viewing counts of nodes. Currently, only <code>Instance</code> is supported.</p>"""
    attribute_name: "aws_sdk_ssm.types.node_attribute_name.NodeAttributeName"
    """<p>The name of a node attribute on which to limit the count of nodes.</p>"""
    aggregators: NotRequired[
        "aws_sdk_ssm.types.node_aggregator_list.NodeAggregatorList"
    ]
    """<p>Information about aggregators used to refine a node summary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeAggregator) -> dict:
    out: dict = {}
    import aws_sdk_ssm.types.node_aggregator_type

    out["AggregatorType"] = (
        aws_sdk_ssm.types.node_aggregator_type.serialize_aws_json_1_1(
            value["aggregator_type"]
        )
    )
    import aws_sdk_ssm.types.node_type_name

    out["TypeName"] = aws_sdk_ssm.types.node_type_name.serialize_aws_json_1_1(
        value["type_name"]
    )
    import aws_sdk_ssm.types.node_attribute_name

    out["AttributeName"] = aws_sdk_ssm.types.node_attribute_name.serialize_aws_json_1_1(
        value["attribute_name"]
    )
    if "aggregators" in value:
        import aws_sdk_ssm.types.node_aggregator_list

        out["Aggregators"] = (
            aws_sdk_ssm.types.node_aggregator_list.serialize_aws_json_1_1(
                value["aggregators"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NodeAggregator:
    out: NodeAggregator = {}  # type: ignore[typeddict-item]
    if "AggregatorType" in data:
        import aws_sdk_ssm.types.node_aggregator_type

        out["aggregator_type"] = (
            aws_sdk_ssm.types.node_aggregator_type.deserialize_aws_json_1_1(
                data["AggregatorType"]
            )
        )
    else:
        raise DeserializationError("NodeAggregator.aggregator_type required")
    if "TypeName" in data:
        import aws_sdk_ssm.types.node_type_name

        out["type_name"] = aws_sdk_ssm.types.node_type_name.deserialize_aws_json_1_1(
            data["TypeName"]
        )
    else:
        raise DeserializationError("NodeAggregator.type_name required")
    if "AttributeName" in data:
        import aws_sdk_ssm.types.node_attribute_name

        out["attribute_name"] = (
            aws_sdk_ssm.types.node_attribute_name.deserialize_aws_json_1_1(
                data["AttributeName"]
            )
        )
    else:
        raise DeserializationError("NodeAggregator.attribute_name required")
    if "Aggregators" in data:
        import aws_sdk_ssm.types.node_aggregator_list

        out["aggregators"] = (
            aws_sdk_ssm.types.node_aggregator_list.deserialize_aws_json_1_1(
                data["Aggregators"]
            )
        )
    return out
