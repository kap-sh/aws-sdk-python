"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailManagedWordList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_managed_word

GuardrailManagedWordList: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.guardrail_managed_word.GuardrailManagedWord"]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailManagedWordList) -> list:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_managed_word
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.guardrail_managed_word.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailManagedWordList:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_managed_word
    out: GuardrailManagedWordList = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.guardrail_managed_word.deserialize_json(item))
    return out