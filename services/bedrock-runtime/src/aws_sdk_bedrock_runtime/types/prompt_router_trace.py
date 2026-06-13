"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#PromptRouterTrace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.invoked_model_id


class PromptRouterTrace(TypedDict):
    invoked_model_id: NotRequired[
        "aws_sdk_bedrock_runtime.types.invoked_model_id.InvokedModelId"
    ]
    """<p>The ID of the invoked model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptRouterTrace) -> dict:
    out: dict = {}
    if "invoked_model_id" in value:
        out["invokedModelId"] = value["invoked_model_id"]
    return out


def deserialize_json(data: dict) -> PromptRouterTrace:
    out: PromptRouterTrace = {}  # type: ignore[typeddict-item]
    if "invokedModelId" in data:
        out["invoked_model_id"] = data["invokedModelId"]
    return out
