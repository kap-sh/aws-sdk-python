"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Resource``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn


class _Resource_arn(TypedDict):
    arn: "aws_sdk_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"


Resource: TypeAlias = _Resource_arn


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    if "arn" in value:
        return {"arn": value["arn"]}
    else:
        raise SerializationError("Resource: no variant present")


def deserialize_json(data: dict) -> Resource:
    if "arn" in data:
        return {"arn": data["arn"]}
    else:
        raise DeserializationError("Resource: no recognized variant key")
