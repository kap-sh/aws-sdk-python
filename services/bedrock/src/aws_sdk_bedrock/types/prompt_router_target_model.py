"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptRouterTargetModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.prompt_router_target_model_arn


class PromptRouterTargetModel(TypedDict, closed=True):
    model_arn: NotRequired[
        "aws_sdk_bedrock.types.prompt_router_target_model_arn.PromptRouterTargetModelArn"
    ]
    """<p>The target model's ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptRouterTargetModel) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["modelArn"] = value["model_arn"]
    return out


def deserialize_json(data: dict) -> PromptRouterTargetModel:
    out: PromptRouterTargetModel = {}  # type: ignore[typeddict-item]
    if "modelArn" in data:
        out["model_arn"] = data["modelArn"]
    return out
