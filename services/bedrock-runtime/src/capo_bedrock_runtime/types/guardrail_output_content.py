"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOutputContent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_output_text


class GuardrailOutputContent(TypedDict, closed=True):
    text: NotRequired[
        "capo_bedrock_runtime.types.guardrail_output_text.GuardrailOutputText"
    ]
    """<p>The specific text for the output content produced by the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailOutputContent) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> GuardrailOutputContent:
    out: GuardrailOutputContent = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out
