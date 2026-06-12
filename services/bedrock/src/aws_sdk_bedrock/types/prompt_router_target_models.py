"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptRouterTargetModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.prompt_router_target_model

PromptRouterTargetModels: TypeAlias = list[
    "aws_sdk_bedrock.types.prompt_router_target_model.PromptRouterTargetModel"
]


# --- restJson1 ser/de ---
def serialize_json(value: PromptRouterTargetModels) -> list:
    import aws_sdk_bedrock.types.prompt_router_target_model

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.prompt_router_target_model.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PromptRouterTargetModels:
    import aws_sdk_bedrock.types.prompt_router_target_model

    out: PromptRouterTargetModels = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.prompt_router_target_model.deserialize_json(item)
        )
    return out
