"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeletePromptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.numerical_version
    import aws_sdk_bedrock_agent.types.prompt_identifier


class DeletePromptRequest(TypedDict, closed=True):
    prompt_identifier: "aws_sdk_bedrock_agent.types.prompt_identifier.PromptIdentifier"
    """<p>The unique identifier of the prompt.</p>"""
    prompt_version: NotRequired[
        "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion"
    ]
    """<p>The version of the prompt to delete. To delete the prompt, omit this field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePromptRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePromptRequest:
    out: DeletePromptRequest = {}  # type: ignore[typeddict-item]
    return out
