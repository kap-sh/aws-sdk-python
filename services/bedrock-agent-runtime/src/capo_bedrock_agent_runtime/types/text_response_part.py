"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TextResponsePart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.span


class TextResponsePart(TypedDict, closed=True):
    text: NotRequired["str"]
    """<p>The part of the generated text that contains a citation.</p>"""
    span: NotRequired["capo_bedrock_agent_runtime.types.span.Span"]
    """<p>Contains information about where the text with a citation begins and ends in the generated output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextResponsePart) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "span" in value:
        import capo_bedrock_agent_runtime.types.span

        out["span"] = capo_bedrock_agent_runtime.types.span.serialize_json(
            value["span"]
        )
    return out


def deserialize_json(data: dict) -> TextResponsePart:
    out: TextResponsePart = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("span") is not None:
        import capo_bedrock_agent_runtime.types.span

        out["span"] = capo_bedrock_agent_runtime.types.span.deserialize_json(
            data["span"]
        )
    return out
