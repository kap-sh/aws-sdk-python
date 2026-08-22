"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailContentFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_content_filter

GuardrailContentFilterList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.guardrail_content_filter.GuardrailContentFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFilterList) -> list:
    import capo_bedrock_agent_runtime.types.guardrail_content_filter

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.guardrail_content_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailContentFilterList:
    import capo_bedrock_agent_runtime.types.guardrail_content_filter

    out: GuardrailContentFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.guardrail_content_filter.deserialize_json(
                item
            )
        )
    return out
