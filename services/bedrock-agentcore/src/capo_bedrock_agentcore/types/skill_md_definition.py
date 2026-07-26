"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SkillMdDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.inline_content


class SkillMdDefinition(TypedDict, closed=True):
    inline_content: NotRequired[
        "capo_bedrock_agentcore.types.inline_content.InlineContent"
    ]
    """<p> The inline markdown content of the skill definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SkillMdDefinition) -> dict:
    out: dict = {}
    if "inline_content" in value:
        out["inlineContent"] = value["inline_content"]
    return out


def deserialize_json(data: dict) -> SkillMdDefinition:
    out: SkillMdDefinition = {}  # type: ignore[typeddict-item]
    if "inlineContent" in data:
        out["inline_content"] = data["inlineContent"]
    return out
