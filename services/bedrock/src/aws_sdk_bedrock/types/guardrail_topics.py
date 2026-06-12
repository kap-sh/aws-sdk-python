"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_topic

GuardrailTopics: TypeAlias = list[
    "aws_sdk_bedrock.types.guardrail_topic.GuardrailTopic"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopics) -> list:
    import aws_sdk_bedrock.types.guardrail_topic

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.guardrail_topic.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailTopics:
    import aws_sdk_bedrock.types.guardrail_topic

    out: GuardrailTopics = []
    for item in data:
        out.append(aws_sdk_bedrock.types.guardrail_topic.deserialize_json(item))
    return out
