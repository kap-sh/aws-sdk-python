"""Generated from Smithy shape ``com.amazonaws.ssm#NodeAttributeName``."""

from typing import Literal, TypeAlias, cast

NodeAttributeName: TypeAlias = Literal[
    "AgentVersion",
    "PlatformName",
    "PlatformType",
    "PlatformVersion",
    "Region",
    "ResourceType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeAttributeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NodeAttributeName:
    return cast(NodeAttributeName, data)
