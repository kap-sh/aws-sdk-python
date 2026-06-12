"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Transformations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.transformation

Transformations: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.transformation.Transformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: Transformations) -> list:
    import aws_sdk_bedrock_agent.types.transformation

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.transformation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Transformations:
    import aws_sdk_bedrock_agent.types.transformation

    out: Transformations = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.transformation.deserialize_json(item))
    return out
