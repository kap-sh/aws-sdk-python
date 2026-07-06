"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RepromptResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.source


class RepromptResponse(TypedDict, closed=True):
    text: NotRequired["str"]
    """<p>The text reprompting the input.</p>"""
    source: NotRequired["aws_sdk_bedrock_agent_runtime.types.source.Source"]
    """<p>Specifies what output is prompting the agent to reprompt the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RepromptResponse) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "source" in value:
        import aws_sdk_bedrock_agent_runtime.types.source

        out["source"] = aws_sdk_bedrock_agent_runtime.types.source.serialize_json(
            value["source"]
        )
    return out


def deserialize_json(data: dict) -> RepromptResponse:
    out: RepromptResponse = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    if "source" in data:
        import aws_sdk_bedrock_agent_runtime.types.source

        out["source"] = aws_sdk_bedrock_agent_runtime.types.source.deserialize_json(
            data["source"]
        )
    return out
