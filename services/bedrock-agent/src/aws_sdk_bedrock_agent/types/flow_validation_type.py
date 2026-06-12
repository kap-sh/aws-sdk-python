"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowValidationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: FlowValidationType) -> str:
    return value


def deserialize_json(data: str) -> FlowValidationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowValidationType value: {data!r}")
    return cast(FlowValidationType, data)
