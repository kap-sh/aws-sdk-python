"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckTranslation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference_list
    import aws_sdk_bedrock.types.automated_reasoning_check_translation_confidence
    import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list


class AutomatedReasoningCheckTranslation(TypedDict):
    premises: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.AutomatedReasoningLogicStatementList"
    ]
    """<p>The logical statements that serve as the foundation or assumptions for the claims.</p>"""
    claims: "aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.AutomatedReasoningLogicStatementList"
    """<p>The logical statements that are being validated against the premises and policy rules.</p>"""
    untranslated_premises: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference_list.AutomatedReasoningCheckInputTextReferenceList"
    ]
    """<p>References to portions of the original input text that correspond to the premises but could not be fully translated.</p>"""
    untranslated_claims: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference_list.AutomatedReasoningCheckInputTextReferenceList"
    ]
    """<p>References to portions of the original input text that correspond to the claims but could not be fully translated.</p>"""
    confidence: "aws_sdk_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
    """<p>A confidence score between 0 and 1 indicating how certain the system is about the logical translation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckTranslation) -> dict:
    out: dict = {}
    if "premises" in value:
        import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list

        out["premises"] = (
            aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.serialize_json(
                value["premises"]
            )
        )
    import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list

    out["claims"] = (
        aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.serialize_json(
            value["claims"]
        )
    )
    if "untranslated_premises" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference_list

        out["untranslatedPremises"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference_list.serialize_json(
                value["untranslated_premises"]
            )
        )
    if "untranslated_claims" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference_list

        out["untranslatedClaims"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference_list.serialize_json(
                value["untranslated_claims"]
            )
        )
    out["confidence"] = value["confidence"]
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckTranslation:
    out: AutomatedReasoningCheckTranslation = {}  # type: ignore[typeddict-item]
    if "premises" in data:
        import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list

        out["premises"] = (
            aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.deserialize_json(
                data["premises"]
            )
        )
    if "claims" in data:
        import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list

        out["claims"] = (
            aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.deserialize_json(
                data["claims"]
            )
        )
    else:
        raise DeserializationError("AutomatedReasoningCheckTranslation.claims required")
    if "untranslatedPremises" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference_list

        out["untranslated_premises"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference_list.deserialize_json(
                data["untranslatedPremises"]
            )
        )
    if "untranslatedClaims" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference_list

        out["untranslated_claims"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_input_text_reference_list.deserialize_json(
                data["untranslatedClaims"]
            )
        )
    if "confidence" in data:
        out["confidence"] = data["confidence"]
    else:
        raise DeserializationError(
            "AutomatedReasoningCheckTranslation.confidence required"
        )
    return out
