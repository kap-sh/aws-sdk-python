"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailContentFilterList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter

GuardrailContentFilterList: TypeAlias = list["aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter.GuardrailContentFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilterList) -> list:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailContentFilterList:
    import aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter
    out: GuardrailContentFilterList = []
    for item in data:
        out.append(aws_sdk_bedrock_agent_runtime.types.guardrail_content_filter.deserialize_json(item))
    return out