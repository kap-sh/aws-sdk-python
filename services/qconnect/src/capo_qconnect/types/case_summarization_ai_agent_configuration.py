"""Generated from Smithy shape ``com.amazonaws.qconnect#CaseSummarizationAIAgentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.uuid_with_qualifier


class CaseSummarizationAIAgentConfiguration(TypedDict, closed=True):
    case_summarization_ai_prompt_id: NotRequired[
        "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Prompt identifier used by the Case Summarization AI Agent.</p>"""
    case_summarization_ai_guardrail_id: NotRequired[
        "capo_qconnect.types.uuid_with_qualifier.UuidWithQualifier"
    ]
    """<p>The AI Guardrail identifier used by the Case Summarization AI Agent.</p>"""
    locale: NotRequired["capo_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The locale setting for the Case Summarization AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CaseSummarizationAIAgentConfiguration) -> dict:
    out: dict = {}
    if "case_summarization_ai_prompt_id" in value:
        out["caseSummarizationAIPromptId"] = value["case_summarization_ai_prompt_id"]
    if "case_summarization_ai_guardrail_id" in value:
        out["caseSummarizationAIGuardrailId"] = value[
            "case_summarization_ai_guardrail_id"
        ]
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_json(data: dict) -> CaseSummarizationAIAgentConfiguration:
    out: CaseSummarizationAIAgentConfiguration = {}  # type: ignore[typeddict-item]
    if "caseSummarizationAIPromptId" in data:
        out["case_summarization_ai_prompt_id"] = data["caseSummarizationAIPromptId"]
    if "caseSummarizationAIGuardrailId" in data:
        out["case_summarization_ai_guardrail_id"] = data[
            "caseSummarizationAIGuardrailId"
        ]
    if "locale" in data:
        out["locale"] = data["locale"]
    return out
