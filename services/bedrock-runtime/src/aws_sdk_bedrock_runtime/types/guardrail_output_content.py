"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailOutputContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_output_text


class GuardrailOutputContent(TypedDict):
    text: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_output_text.GuardrailOutputText"
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
    if "text" in data:
        out["text"] = data["text"]
    return out
