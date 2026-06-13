"""Generated from Smithy shape ``com.amazonaws.qconnect#NoteTakingAIAgentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.uuid_with_qualifier


class NoteTakingAIAgentConfiguration(TypedDict):
    note_taking_ai_prompt_id: NotRequired[
        "aws_sdk_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Prompt identifier used by the Note Taking AI Agent.</p>"""
    note_taking_ai_guardrail_id: NotRequired[
        "aws_sdk_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Guardrail identifier used by the Note Taking AI Agent.</p>"""
    locale: NotRequired["aws_sdk_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The locale setting for language-specific case summarization generation (for example, en_US, es_ES).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NoteTakingAIAgentConfiguration) -> dict:
    out: dict = {}
    if "note_taking_ai_prompt_id" in value:
        out["noteTakingAIPromptId"] = value["note_taking_ai_prompt_id"]
    if "note_taking_ai_guardrail_id" in value:
        out["noteTakingAIGuardrailId"] = value["note_taking_ai_guardrail_id"]
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_json(data: dict) -> NoteTakingAIAgentConfiguration:
    out: NoteTakingAIAgentConfiguration = {}  # type: ignore[typeddict-item]
    if "noteTakingAIPromptId" in data:
        out["note_taking_ai_prompt_id"] = data["noteTakingAIPromptId"]
    if "noteTakingAIGuardrailId" in data:
        out["note_taking_ai_guardrail_id"] = data["noteTakingAIGuardrailId"]
    if "locale" in data:
        out["locale"] = data["locale"]
    return out
