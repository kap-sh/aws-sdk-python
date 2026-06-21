"""Generated from Smithy shape ``com.amazonaws.ssm#NodeAggregatorType``."""

from typing import Literal, TypeAlias, cast

NodeAggregatorType: TypeAlias = Literal["Count",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeAggregatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeAggregatorType:
    return cast(NodeAggregatorType, data)
