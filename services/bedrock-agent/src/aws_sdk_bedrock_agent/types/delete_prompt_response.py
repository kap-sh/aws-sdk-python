"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeletePromptResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.numerical_version
    import aws_sdk_bedrock_agent.types.prompt_id


class DeletePromptResponse(TypedDict):
    id: "aws_sdk_bedrock_agent.types.prompt_id.PromptId"
    """<p>The unique identifier of the prompt that was deleted.</p>"""
    version: NotRequired[
        "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion"
    ]
    """<p>The version of the prompt that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePromptResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> DeletePromptResponse:
    out: DeletePromptResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeletePromptResponse.id required")
    if "version" in data:
        out["version"] = data["version"]
    return out
