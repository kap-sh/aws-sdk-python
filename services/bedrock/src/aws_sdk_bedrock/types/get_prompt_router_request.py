"""Generated from Smithy shape ``com.amazonaws.bedrock#GetPromptRouterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.prompt_router_arn


class GetPromptRouterRequest(TypedDict, closed=True):
    prompt_router_arn: "aws_sdk_bedrock.types.prompt_router_arn.PromptRouterArn"
    """<p>The prompt router's ARN</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPromptRouterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPromptRouterRequest:
    out: GetPromptRouterRequest = {}  # type: ignore[typeddict-item]
    return out
