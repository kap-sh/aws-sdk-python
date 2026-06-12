"""Generated from Smithy shape ``com.amazonaws.ssm#NodeAggregatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.node_aggregator

NodeAggregatorList: TypeAlias = list["aws_sdk_ssm.types.node_aggregator.NodeAggregator"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeAggregatorList) -> list:
    import aws_sdk_ssm.types.node_aggregator

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.node_aggregator.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NodeAggregatorList:
    import aws_sdk_ssm.types.node_aggregator

    out: NodeAggregatorList = []
    for item in data:
        out.append(aws_sdk_ssm.types.node_aggregator.deserialize_aws_json_1_1(item))
    return out
