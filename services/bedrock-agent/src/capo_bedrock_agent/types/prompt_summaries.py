"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.prompt_summary

PromptSummaries: TypeAlias = list[
    "capo_bedrock_agent.types.prompt_summary.PromptSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptSummaries) -> list:
    import capo_bedrock_agent.types.prompt_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.prompt_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromptSummaries:
    import capo_bedrock_agent.types.prompt_summary

    out: PromptSummaries = []
    for item in data:
        out.append(capo_bedrock_agent.types.prompt_summary.deserialize_json(item))
    return out
