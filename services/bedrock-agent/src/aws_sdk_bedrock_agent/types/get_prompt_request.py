"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetPromptRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.prompt_identifier
    import aws_sdk_bedrock_agent.types.version


class GetPromptRequest(TypedDict):
    prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier"
    """<p>The unique identifier of the prompt.</p>"""
    prompt_version: NotRequired["aws_sdk_bedrock_agent.types.version.Version"]
    """<p>The version of the prompt about which you want to retrieve information. Omit this field to return information about the working draft of the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPromptRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPromptRequest:
    out: GetPromptRequest = {}  # type: ignore[typeddict-item]
    return out
