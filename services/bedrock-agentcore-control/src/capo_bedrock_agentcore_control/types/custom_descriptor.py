"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inline_content


class CustomDescriptor(TypedDict, closed=True):
    inline_content: NotRequired[
        "capo_bedrock_agentcore_control.types.inline_content.InlineContent"
    ]
    """<p>The custom descriptor content as a valid JSON document. You can define any custom schema that describes your resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDescriptor) -> dict:
    out: dict = {}
    if "inline_content" in value:
        out["inlineContent"] = value["inline_content"]
    return out


def deserialize_json(data: dict) -> CustomDescriptor:
    out: CustomDescriptor = {}  # type: ignore[typeddict-item]
    if "inlineContent" in data:
        out["inline_content"] = data["inlineContent"]
    return out
