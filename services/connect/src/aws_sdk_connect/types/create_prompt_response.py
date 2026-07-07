"""Generated from Smithy shape ``com.amazonaws.connect#CreatePromptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.prompt_id


class CreatePromptResponse(TypedDict, closed=True):
    prompt_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the prompt.</p>"""
    prompt_id: NotRequired["aws_sdk_connect.types.prompt_id.PromptId"]
    """<p>A unique identifier for the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePromptResponse) -> dict:
    out: dict = {}
    if "prompt_arn" in value:
        out["PromptARN"] = value["prompt_arn"]
    if "prompt_id" in value:
        out["PromptId"] = value["prompt_id"]
    return out


def deserialize_json(data: dict) -> CreatePromptResponse:
    out: CreatePromptResponse = {}  # type: ignore[typeddict-item]
    if "PromptARN" in data:
        out["prompt_arn"] = data["PromptARN"]
    if "PromptId" in data:
        out["prompt_id"] = data["PromptId"]
    return out
