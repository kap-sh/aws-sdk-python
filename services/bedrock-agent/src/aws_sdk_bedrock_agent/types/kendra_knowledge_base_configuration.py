"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KendraKnowledgeBaseConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.kendra_index_arn


class KendraKnowledgeBaseConfiguration(TypedDict):
    kendra_index_arn: "aws_sdk_bedrock_agent.types.kendra_index_arn.KendraIndexArn"
    """<p>The ARN of the Amazon Kendra index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KendraKnowledgeBaseConfiguration) -> dict:
    out: dict = {}
    out["kendraIndexArn"] = value["kendra_index_arn"]
    return out


def deserialize_json(data: dict) -> KendraKnowledgeBaseConfiguration:
    out: KendraKnowledgeBaseConfiguration = {}  # type: ignore[typeddict-item]
    if "kendraIndexArn" in data:
        out["kendra_index_arn"] = data["kendraIndexArn"]
    else:
        raise DeserializationError(
            "KendraKnowledgeBaseConfiguration.kendra_index_arn required"
        )
    return out
