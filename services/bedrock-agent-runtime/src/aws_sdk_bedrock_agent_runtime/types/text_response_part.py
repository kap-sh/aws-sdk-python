"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TextResponsePart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.span


class TextResponsePart(TypedDict, closed=True):
    text: NotRequired["str"]
    """<p>The part of the generated text that contains a citation.</p>"""
    span: NotRequired["aws_sdk_bedrock_agent_runtime.types.span.Span"]
    """<p>Contains information about where the text with a citation begins and ends in the generated output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextResponsePart) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "span" in value:
        import aws_sdk_bedrock_agent_runtime.types.span

        out["span"] = aws_sdk_bedrock_agent_runtime.types.span.serialize_json(
            value["span"]
        )
    return out


def deserialize_json(data: dict) -> TextResponsePart:
    out: TextResponsePart = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    if "span" in data:
        import aws_sdk_bedrock_agent_runtime.types.span

        out["span"] = aws_sdk_bedrock_agent_runtime.types.span.deserialize_json(
            data["span"]
        )
    return out
