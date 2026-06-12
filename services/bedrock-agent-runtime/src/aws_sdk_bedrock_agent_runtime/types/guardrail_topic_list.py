"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailTopicList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_topic

GuardrailTopicList: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.guardrail_topic.GuardrailTopic"]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicList) -> list:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_topic
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.guardrail_topic.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailTopicList:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_topic
    out: GuardrailTopicList = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.guardrail_topic.deserialize_json(item))
    return out