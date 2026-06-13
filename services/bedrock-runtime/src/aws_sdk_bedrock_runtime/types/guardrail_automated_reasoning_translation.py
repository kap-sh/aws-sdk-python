"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningTranslation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_confidence


class GuardrailAutomatedReasoningTranslation(TypedDict):
    premises: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.GuardrailAutomatedReasoningStatementList"
    ]
    """<p>The logical statements that serve as the foundation or assumptions for the claims.</p>"""
    claims: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.GuardrailAutomatedReasoningStatementList"
    ]
    """<p>The logical statements that are being validated against the premises and policy rules.</p>"""
    untranslated_premises: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.GuardrailAutomatedReasoningInputTextReferenceList"
    ]
    """<p>References to portions of the original input text that correspond to the premises but could not be fully translated.</p>"""
    untranslated_claims: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.GuardrailAutomatedReasoningInputTextReferenceList"
    ]
    """<p>References to portions of the original input text that correspond to the claims but could not be fully translated.</p>"""
    confidence: NotRequired[
        "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_confidence.GuardrailAutomatedReasoningTranslationConfidence"
    ]
    """<p>A confidence score between 0 and 1 indicating how certain the system is about the logical translation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningTranslation) -> dict:
    out: dict = {}
    if "premises" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["premises"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.serialize_json(
                value["premises"]
            )
        )
    if "claims" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["claims"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.serialize_json(
                value["claims"]
            )
        )
    if "untranslated_premises" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list

        out["untranslatedPremises"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.serialize_json(
                value["untranslated_premises"]
            )
        )
    if "untranslated_claims" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list

        out["untranslatedClaims"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.serialize_json(
                value["untranslated_claims"]
            )
        )
    if "confidence" in value:
        out["confidence"] = value["confidence"]
    return out


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningTranslation:
    out: GuardrailAutomatedReasoningTranslation = {}  # type: ignore[typeddict-item]
    if "premises" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["premises"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.deserialize_json(
                data["premises"]
            )
        )
    if "claims" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list

        out["claims"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_statement_list.deserialize_json(
                data["claims"]
            )
        )
    if "untranslatedPremises" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list

        out["untranslated_premises"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.deserialize_json(
                data["untranslatedPremises"]
            )
        )
    if "untranslatedClaims" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list

        out["untranslated_claims"] = (
            aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_input_text_reference_list.deserialize_json(
                data["untranslatedClaims"]
            )
        )
    if "confidence" in data:
        out["confidence"] = data["confidence"]
    return out
