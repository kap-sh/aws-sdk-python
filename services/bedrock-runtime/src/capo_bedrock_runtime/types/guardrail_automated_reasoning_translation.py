"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningTranslation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_list
    import capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_confidence


class GuardrailAutomatedReasoningTranslation(TypedDict, closed=True):
    premises: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.GuardrailAutomatedReasoningStatementList"
    ]
    """<p>The logical statements that serve as the foundation or assumptions for the claims.</p>"""
    claims: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.GuardrailAutomatedReasoningStatementList"
    ]
    """<p>The logical statements that are being validated against the premises and policy rules.</p>"""
    untranslated_premises: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.GuardrailAutomatedReasoningInputTextReferenceList"
    ]
    """<p>References to portions of the original input text that correspond to the premises but could not be fully translated.</p>"""
    untranslated_claims: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.GuardrailAutomatedReasoningInputTextReferenceList"
    ]
    """<p>References to portions of the original input text that correspond to the claims but could not be fully translated.</p>"""
    confidence: NotRequired[
        "capo_bedrock_runtime.types.guardrail_automated_reasoning_translation_confidence.GuardrailAutomatedReasoningTranslationConfidence"
    ]
    """<p>A confidence score between 0 and 1 indicating how certain the system is about the logical translation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningTranslation) -> dict:
    out: dict = {}
    if "premises" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["premises"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.serialize_json(
                value["premises"]
            )
        )
    if "claims" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["claims"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.serialize_json(
                value["claims"]
            )
        )
    if "untranslated_premises" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list

        out["untranslatedPremises"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.serialize_json(
                value["untranslated_premises"]
            )
        )
    if "untranslated_claims" in value:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list

        out["untranslatedClaims"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.serialize_json(
                value["untranslated_claims"]
            )
        )
    if "confidence" in value:
        out["confidence"] = value["confidence"]
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningTranslation:
    out: GuardrailAutomatedReasoningTranslation = {}  # type: ignore[typeddict-item]
    if "premises" in data:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["premises"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.deserialize_json(
                data["premises"]
            )
        )
    if "claims" in data:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["claims"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.deserialize_json(
                data["claims"]
            )
        )
    if "untranslatedPremises" in data:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list

        out["untranslated_premises"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.deserialize_json(
                data["untranslatedPremises"]
            )
        )
    if "untranslatedClaims" in data:
        import capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list

        out["untranslated_claims"] = (
            capo_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.deserialize_json(
                data["untranslatedClaims"]
            )
        )
    if "confidence" in data:
        out["confidence"] = data["confidence"]
    return out
