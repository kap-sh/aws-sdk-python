"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GuardrailRegexFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_regex_filter

GuardrailRegexFilterList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.guardrail_regex_filter.GuardrailRegexFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegexFilterList) -> list:
    import capo_bedrock_agent_runtime.types.guardrail_regex_filter

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.guardrail_regex_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailRegexFilterList:
    import capo_bedrock_agent_runtime.types.guardrail_regex_filter

    out: GuardrailRegexFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.guardrail_regex_filter.deserialize_json(
                item
            )
        )
    return out
