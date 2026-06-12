"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckFinding``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_satisfiable_finding
    import aws_sdk_bedrock.types.automated_reasoning_check_translation_ambiguous_finding
    import aws_sdk_bedrock.types.automated_reasoning_check_impossible_finding
    import aws_sdk_bedrock.types.automated_reasoning_check_valid_finding
    import aws_sdk_bedrock.types.automated_reasoning_check_too_complex_finding
    import aws_sdk_bedrock.types.automated_reasoning_check_invalid_finding
    import aws_sdk_bedrock.types.automated_reasoning_check_no_translations_finding


class _AutomatedReasoningCheckFinding_valid(TypedDict):
    valid: "aws_sdk_bedrock.types.automated_reasoning_check_valid_finding.AutomatedReasoningCheckValidFinding"


class _AutomatedReasoningCheckFinding_invalid(TypedDict):
    invalid: "aws_sdk_bedrock.types.automated_reasoning_check_invalid_finding.AutomatedReasoningCheckInvalidFinding"


class _AutomatedReasoningCheckFinding_satisfiable(TypedDict):
    satisfiable: "aws_sdk_bedrock.types.automated_reasoning_check_satisfiable_finding.AutomatedReasoningCheckSatisfiableFinding"


class _AutomatedReasoningCheckFinding_impossible(TypedDict):
    impossible: "aws_sdk_bedrock.types.automated_reasoning_check_impossible_finding.AutomatedReasoningCheckImpossibleFinding"


class _AutomatedReasoningCheckFinding_translationAmbiguous(TypedDict):
    translationAmbiguous: "aws_sdk_bedrock.types.automated_reasoning_check_translation_ambiguous_finding.AutomatedReasoningCheckTranslationAmbiguousFinding"


class _AutomatedReasoningCheckFinding_tooComplex(TypedDict):
    tooComplex: "aws_sdk_bedrock.types.automated_reasoning_check_too_complex_finding.AutomatedReasoningCheckTooComplexFinding"


class _AutomatedReasoningCheckFinding_noTranslations(TypedDict):
    noTranslations: "aws_sdk_bedrock.types.automated_reasoning_check_no_translations_finding.AutomatedReasoningCheckNoTranslationsFinding"


AutomatedReasoningCheckFinding: TypeAlias = (
    _AutomatedReasoningCheckFinding_valid
    | _AutomatedReasoningCheckFinding_invalid
    | _AutomatedReasoningCheckFinding_satisfiable
    | _AutomatedReasoningCheckFinding_impossible
    | _AutomatedReasoningCheckFinding_translationAmbiguous
    | _AutomatedReasoningCheckFinding_tooComplex
    | _AutomatedReasoningCheckFinding_noTranslations
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckFinding) -> dict:
    if "valid" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_valid_finding

        return {
            "valid": aws_sdk_bedrock.types.automated_reasoning_check_valid_finding.serialize_json(
                value["valid"]
            )
        }
    elif "invalid" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_invalid_finding

        return {
            "invalid": aws_sdk_bedrock.types.automated_reasoning_check_invalid_finding.serialize_json(
                value["invalid"]
            )
        }
    elif "satisfiable" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_satisfiable_finding

        return {
            "satisfiable": aws_sdk_bedrock.types.automated_reasoning_check_satisfiable_finding.serialize_json(
                value["satisfiable"]
            )
        }
    elif "impossible" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_impossible_finding

        return {
            "impossible": aws_sdk_bedrock.types.automated_reasoning_check_impossible_finding.serialize_json(
                value["impossible"]
            )
        }
    elif "translationAmbiguous" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_translation_ambiguous_finding

        return {
            "translationAmbiguous": aws_sdk_bedrock.types.automated_reasoning_check_translation_ambiguous_finding.serialize_json(
                value["translationAmbiguous"]
            )
        }
    elif "tooComplex" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_too_complex_finding

        return {
            "tooComplex": aws_sdk_bedrock.types.automated_reasoning_check_too_complex_finding.serialize_json(
                value["tooComplex"]
            )
        }
    elif "noTranslations" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_no_translations_finding

        return {
            "noTranslations": aws_sdk_bedrock.types.automated_reasoning_check_no_translations_finding.serialize_json(
                value["noTranslations"]
            )
        }
    else:
        raise SerializationError("AutomatedReasoningCheckFinding: no variant present")


def deserialize_json(data: dict) -> AutomatedReasoningCheckFinding:
    if "valid" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_valid_finding

        return {
            "valid": aws_sdk_bedrock.types.automated_reasoning_check_valid_finding.deserialize_json(
                data["valid"]
            )
        }
    elif "invalid" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_invalid_finding

        return {
            "invalid": aws_sdk_bedrock.types.automated_reasoning_check_invalid_finding.deserialize_json(
                data["invalid"]
            )
        }
    elif "satisfiable" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_satisfiable_finding

        return {
            "satisfiable": aws_sdk_bedrock.types.automated_reasoning_check_satisfiable_finding.deserialize_json(
                data["satisfiable"]
            )
        }
    elif "impossible" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_impossible_finding

        return {
            "impossible": aws_sdk_bedrock.types.automated_reasoning_check_impossible_finding.deserialize_json(
                data["impossible"]
            )
        }
    elif "translationAmbiguous" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_translation_ambiguous_finding

        return {
            "translationAmbiguous": aws_sdk_bedrock.types.automated_reasoning_check_translation_ambiguous_finding.deserialize_json(
                data["translationAmbiguous"]
            )
        }
    elif "tooComplex" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_too_complex_finding

        return {
            "tooComplex": aws_sdk_bedrock.types.automated_reasoning_check_too_complex_finding.deserialize_json(
                data["tooComplex"]
            )
        }
    elif "noTranslations" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_no_translations_finding

        return {
            "noTranslations": aws_sdk_bedrock.types.automated_reasoning_check_no_translations_finding.deserialize_json(
                data["noTranslations"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningCheckFinding: no recognized variant key"
        )
