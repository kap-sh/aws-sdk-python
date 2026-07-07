"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailAutomatedReasoningFinding``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding
    import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding


class _GuardrailAutomatedReasoningFinding_valid(TypedDict, closed=True):
    valid: "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding.GuardrailAutomatedReasoningValidFinding"


class _GuardrailAutomatedReasoningFinding_invalid(TypedDict, closed=True):
    invalid: "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding.GuardrailAutomatedReasoningInvalidFinding"


class _GuardrailAutomatedReasoningFinding_satisfiable(TypedDict, closed=True):
    satisfiable: "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding.GuardrailAutomatedReasoningSatisfiableFinding"


class _GuardrailAutomatedReasoningFinding_impossible(TypedDict, closed=True):
    impossible: "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding.GuardrailAutomatedReasoningImpossibleFinding"


class _GuardrailAutomatedReasoningFinding_translationAmbiguous(TypedDict, closed=True):
    translationAmbiguous: "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding.GuardrailAutomatedReasoningTranslationAmbiguousFinding"


class _GuardrailAutomatedReasoningFinding_tooComplex(TypedDict, closed=True):
    tooComplex: "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding.GuardrailAutomatedReasoningTooComplexFinding"


class _GuardrailAutomatedReasoningFinding_noTranslations(TypedDict, closed=True):
    noTranslations: "aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding.GuardrailAutomatedReasoningNoTranslationsFinding"


GuardrailAutomatedReasoningFinding: TypeAlias = (
    _GuardrailAutomatedReasoningFinding_valid
    | _GuardrailAutomatedReasoningFinding_invalid
    | _GuardrailAutomatedReasoningFinding_satisfiable
    | _GuardrailAutomatedReasoningFinding_impossible
    | _GuardrailAutomatedReasoningFinding_translationAmbiguous
    | _GuardrailAutomatedReasoningFinding_tooComplex
    | _GuardrailAutomatedReasoningFinding_noTranslations
)


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailAutomatedReasoningFinding) -> dict:
    if "valid" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding

        return {
            "valid": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding.serialize_json(
                value["valid"]
            )
        }
    elif "invalid" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding

        return {
            "invalid": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding.serialize_json(
                value["invalid"]
            )
        }
    elif "satisfiable" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding

        return {
            "satisfiable": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding.serialize_json(
                value["satisfiable"]
            )
        }
    elif "impossible" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding

        return {
            "impossible": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding.serialize_json(
                value["impossible"]
            )
        }
    elif "translationAmbiguous" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding

        return {
            "translationAmbiguous": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding.serialize_json(
                value["translationAmbiguous"]
            )
        }
    elif "tooComplex" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding

        return {
            "tooComplex": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding.serialize_json(
                value["tooComplex"]
            )
        }
    elif "noTranslations" in value:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding

        return {
            "noTranslations": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding.serialize_json(
                value["noTranslations"]
            )
        }
    else:
        raise SerializationError(
            "GuardrailAutomatedReasoningFinding: no variant present"
        )


def deserialize_json(data: dict) -> GuardrailAutomatedReasoningFinding:
    if "valid" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding

        return {
            "valid": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_valid_finding.deserialize_json(
                data["valid"]
            )
        }
    elif "invalid" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding

        return {
            "invalid": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_invalid_finding.deserialize_json(
                data["invalid"]
            )
        }
    elif "satisfiable" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding

        return {
            "satisfiable": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_satisfiable_finding.deserialize_json(
                data["satisfiable"]
            )
        }
    elif "impossible" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding

        return {
            "impossible": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_impossible_finding.deserialize_json(
                data["impossible"]
            )
        }
    elif "translationAmbiguous" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding

        return {
            "translationAmbiguous": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_translation_ambiguous_finding.deserialize_json(
                data["translationAmbiguous"]
            )
        }
    elif "tooComplex" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding

        return {
            "tooComplex": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_too_complex_finding.deserialize_json(
                data["tooComplex"]
            )
        }
    elif "noTranslations" in data:
        import aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding

        return {
            "noTranslations": aws_sdk_bedrock_runtime.types.guardrail_automated_reasoning_no_translations_finding.deserialize_json(
                data["noTranslations"]
            )
        }
    else:
        raise DeserializationError(
            "GuardrailAutomatedReasoningFinding: no recognized variant key"
        )
