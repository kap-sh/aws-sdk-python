"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptRouterSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.prompt_router_summary

PromptRouterSummaries: TypeAlias = list[
    "capo_bedrock.types.prompt_router_summary.PromptRouterSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptRouterSummaries) -> list:
    import capo_bedrock.types.prompt_router_summary

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.prompt_router_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromptRouterSummaries:
    import capo_bedrock.types.prompt_router_summary

    out: PromptRouterSummaries = []
    for item in data:
        out.append(capo_bedrock.types.prompt_router_summary.deserialize_json(item))
    return out
