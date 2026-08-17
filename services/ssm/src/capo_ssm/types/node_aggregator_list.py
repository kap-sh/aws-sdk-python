"""Generated from Smithy shape ``com.amazonaws.ssm#NodeAggregatorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.node_aggregator

NodeAggregatorList: TypeAlias = list["capo_ssm.types.node_aggregator.NodeAggregator"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeAggregatorList) -> list:
    import capo_ssm.types.node_aggregator

    out: list = []
    for item in value:
        out.append(capo_ssm.types.node_aggregator.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NodeAggregatorList:
    import capo_ssm.types.node_aggregator

    out: NodeAggregatorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.node_aggregator.deserialize_aws_json_1_1(item))
    return out
