"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptRouterTargetModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.prompt_router_target_model

PromptRouterTargetModels: TypeAlias = list[
    "capo_bedrock.types.prompt_router_target_model.PromptRouterTargetModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptRouterTargetModels) -> list:
    import capo_bedrock.types.prompt_router_target_model

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.prompt_router_target_model.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromptRouterTargetModels:
    import capo_bedrock.types.prompt_router_target_model

    out: PromptRouterTargetModels = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.prompt_router_target_model.deserialize_json(item))
    return out
