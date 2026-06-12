"""Generated from Smithy shape ``com.amazonaws.bedrock#DeletePromptRouterRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.prompt_router_arn


class DeletePromptRouterRequest(TypedDict):
    prompt_router_arn: "aws_sdk_bedrock.types.prompt_router_arn.PromptRouterArn"
    """<p>The Amazon Resource Name (ARN) of the prompt router to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePromptRouterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePromptRouterRequest:
    out: DeletePromptRouterRequest = {}  # type: ignore[typeddict-item]
    return out
