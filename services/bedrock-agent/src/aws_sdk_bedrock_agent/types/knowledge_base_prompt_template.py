"""Generated from Smithy shape ``com.amazonaws.bedrockagent#KnowledgeBasePromptTemplate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.knowledge_base_text_prompt


class KnowledgeBasePromptTemplate(TypedDict):
    text_prompt_template: NotRequired[
        "aws_sdk_bedrock_agent.types.knowledge_base_text_prompt.KnowledgeBaseTextPrompt"
    ]
    """<p>The text of the prompt template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBasePromptTemplate) -> dict:
    out: dict = {}
    if "text_prompt_template" in value:
        out["textPromptTemplate"] = value["text_prompt_template"]
    return out


def deserialize_json(data: dict) -> KnowledgeBasePromptTemplate:
    out: KnowledgeBasePromptTemplate = {}  # type: ignore[typeddict-item]
    if "textPromptTemplate" in data:
        out["text_prompt_template"] = data["textPromptTemplate"]
    return out
