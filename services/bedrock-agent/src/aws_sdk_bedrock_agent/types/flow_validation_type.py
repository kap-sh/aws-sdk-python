"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowValidationType``."""

from typing import Literal, TypeAlias, cast

FlowValidationType: TypeAlias = Literal[
    "CyclicConnection",
    "DuplicateConnections",
    "DuplicateConditionExpression",
    "UnreachableNode",
    "UnknownConnectionSource",
    "UnknownConnectionSourceOutput",
    "UnknownConnectionTarget",
    "UnknownConnectionTargetInput",
    "UnknownConnectionCondition",
    "MalformedConditionExpression",
    "MalformedNodeInputExpression",
    "MismatchedNodeInputType",
    "MismatchedNodeOutputType",
    "IncompatibleConnectionDataType",
    "MissingConnectionConfiguration",
    "MissingDefaultCondition",
    "MissingEndingNodes",
    "MissingNodeConfiguration",
    "MissingNodeInput",
    "MissingNodeOutput",
    "MissingStartingNodes",
    "MultipleNodeInputConnections",
    "UnfulfilledNodeInput",
    "UnsatisfiedConnectionConditions",
    "Unspecified",
    "UnknownNodeInput",
    "UnknownNodeOutput",
    "MissingLoopInputNode",
    "MissingLoopControllerNode",
    "MultipleLoopInputNodes",
    "MultipleLoopControllerNodes",
    "LoopIncompatibleNodeType",
    "InvalidLoopBoundary",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowValidationType) -> str:
    return value


def deserialize_json(data: str) -> FlowValidationType:
    return cast(FlowValidationType, data)
