"""Generated from Smithy shape ``com.amazonaws.detective#GraphArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_detective.types.graph_arn

GraphArnList: TypeAlias = list["aws_sdk_detective.types.graph_arn.GraphArn"]


# --- restJson1 ser/de ---
def serialize_json(value: GraphArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> GraphArnList:
    return list(data)
