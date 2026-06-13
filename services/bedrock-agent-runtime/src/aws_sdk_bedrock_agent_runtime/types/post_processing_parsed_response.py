"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PostProcessingParsedResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.output_string


class PostProcessingParsedResponse(TypedDict):
    text: NotRequired["aws_sdk_bedrock_agent_runtime.types.output_string.OutputString"]
    """<p>The text returned by the parser.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostProcessingParsedResponse) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> PostProcessingParsedResponse:
    out: PostProcessingParsedResponse = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    return out
