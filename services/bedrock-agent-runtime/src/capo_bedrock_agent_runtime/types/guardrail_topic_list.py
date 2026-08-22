"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailTopicList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_topic

GuardrailTopicList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.guardrail_topic.GuardrailTopic"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicList) -> list:
    import capo_bedrock_agent_runtime.types.guardrail_topic

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.guardrail_topic.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailTopicList:
    import capo_bedrock_agent_runtime.types.guardrail_topic

    out: GuardrailTopicList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.guardrail_topic.deserialize_json(item)
        )
    return out
