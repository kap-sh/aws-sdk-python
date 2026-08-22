"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PostProcessingParsedResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.output_string


class PostProcessingParsedResponse(TypedDict, closed=True):
    text: NotRequired["capo_bedrock_agent_runtime.types.output_string.OutputString"]
    """<p>The text returned by the parser.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostProcessingParsedResponse) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> PostProcessingParsedResponse:
    out: PostProcessingParsedResponse = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out
