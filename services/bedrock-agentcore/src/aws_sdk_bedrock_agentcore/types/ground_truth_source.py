"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GroundTruthSource``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.inline_ground_truth

class _GroundTruthSource_inline(TypedDict):
    inline: "aws_sdk_bedrock_agentcore.types.inline_ground_truth.InlineGroundTruth"

GroundTruthSource: TypeAlias = _GroundTruthSource_inline

# --- restJson1 ser/de ---
def serialize_json(value: GroundTruthSource) -> dict:
    if "inline" in value:
        import aws_sdk_bedrock_agentcore.types.inline_ground_truth
        return {"inline": aws_sdk_bedrock_agentcore.types.inline_ground_truth.serialize_json(value["inline"])}
    else:
        raise SerializationError("GroundTruthSource: no variant present")


def deserialize_json(data: dict) -> GroundTruthSource:
    if "inline" in data:
        import aws_sdk_bedrock_agentcore.types.inline_ground_truth
        return {"inline": aws_sdk_bedrock_agentcore.types.inline_ground_truth.deserialize_json(data["inline"])}
    else:
        raise DeserializationError("GroundTruthSource: no recognized variant key")