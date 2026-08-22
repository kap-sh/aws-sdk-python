"""Generated from Smithy shape ``com.amazonaws.bedrock#CreatePromptRouterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.prompt_router_arn


class CreatePromptRouterResponse(TypedDict, closed=True):
    prompt_router_arn: NotRequired[
        "capo_bedrock.types.prompt_router_arn.PromptRouterArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the prompt router.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePromptRouterResponse) -> dict:
    out: dict = {}
    if "prompt_router_arn" in value:
        out["promptRouterArn"] = value["prompt_router_arn"]
    return out


def deserialize_json(data: dict) -> CreatePromptRouterResponse:
    out: CreatePromptRouterResponse = {}  # type: ignore[typeddict-item]
    if data.get("promptRouterArn") is not None:
        out["prompt_router_arn"] = data["promptRouterArn"]
    return out
