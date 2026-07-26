"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckFinding``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_impossible_finding
    import capo_bedrock.types.automated_reasoning_check_invalid_finding
    import capo_bedrock.types.automated_reasoning_check_no_translations_finding
    import capo_bedrock.types.automated_reasoning_check_satisfiable_finding
    import capo_bedrock.types.automated_reasoning_check_too_complex_finding
    import capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding
    import capo_bedrock.types.automated_reasoning_check_valid_finding


class _AutomatedReasoningCheckFinding_valid(TypedDict, closed=True):
    valid: "capo_bedrock.types.automated_reasoning_check_valid_finding.AutomatedReasoningCheckValidFinding"


class _AutomatedReasoningCheckFinding_invalid(TypedDict, closed=True):
    invalid: "capo_bedrock.types.automated_reasoning_check_invalid_finding.AutomatedReasoningCheckInvalidFinding"


class _AutomatedReasoningCheckFinding_satisfiable(TypedDict, closed=True):
    satisfiable: "capo_bedrock.types.automated_reasoning_check_satisfiable_finding.AutomatedReasoningCheckSatisfiableFinding"


class _AutomatedReasoningCheckFinding_impossible(TypedDict, closed=True):
    impossible: "capo_bedrock.types.automated_reasoning_check_impossible_finding.AutomatedReasoningCheckImpossibleFinding"


class _AutomatedReasoningCheckFinding_translationAmbiguous(TypedDict, closed=True):
    translationAmbiguous: "capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding.AutomatedReasoningCheckTranslationAmbiguousFinding"


class _AutomatedReasoningCheckFinding_tooComplex(TypedDict, closed=True):
    tooComplex: "capo_bedrock.types.automated_reasoning_check_too_complex_finding.AutomatedReasoningCheckTooComplexFinding"


class _AutomatedReasoningCheckFinding_noTranslations(TypedDict, closed=True):
    noTranslations: "capo_bedrock.types.automated_reasoning_check_no_translations_finding.AutomatedReasoningCheckNoTranslationsFinding"


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
        import capo_bedrock.types.automated_reasoning_check_valid_finding

        return {
            "valid": capo_bedrock.types.automated_reasoning_check_valid_finding.serialize_json(
                value["valid"]
            )
        }
    elif "invalid" in value:
        import capo_bedrock.types.automated_reasoning_check_invalid_finding

        return {
            "invalid": capo_bedrock.types.automated_reasoning_check_invalid_finding.serialize_json(
                value["invalid"]
            )
        }
    elif "satisfiable" in value:
        import capo_bedrock.types.automated_reasoning_check_satisfiable_finding

        return {
            "satisfiable": capo_bedrock.types.automated_reasoning_check_satisfiable_finding.serialize_json(
                value["satisfiable"]
            )
        }
    elif "impossible" in value:
        import capo_bedrock.types.automated_reasoning_check_impossible_finding

        return {
            "impossible": capo_bedrock.types.automated_reasoning_check_impossible_finding.serialize_json(
                value["impossible"]
            )
        }
    elif "translationAmbiguous" in value:
        import capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding

        return {
            "translationAmbiguous": capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding.serialize_json(
                value["translationAmbiguous"]
            )
        }
    elif "tooComplex" in value:
        import capo_bedrock.types.automated_reasoning_check_too_complex_finding

        return {
            "tooComplex": capo_bedrock.types.automated_reasoning_check_too_complex_finding.serialize_json(
                value["tooComplex"]
            )
        }
    elif "noTranslations" in value:
        import capo_bedrock.types.automated_reasoning_check_no_translations_finding

        return {
            "noTranslations": capo_bedrock.types.automated_reasoning_check_no_translations_finding.serialize_json(
                value["noTranslations"]
            )
        }
    else:
        raise SerializationError("AutomatedReasoningCheckFinding: no variant present")


def deserialize_json(data: dict) -> AutomatedReasoningCheckFinding:
    if "valid" in data:
        import capo_bedrock.types.automated_reasoning_check_valid_finding

        return {
            "valid": capo_bedrock.types.automated_reasoning_check_valid_finding.deserialize_json(
                data["valid"]
            )
        }
    elif "invalid" in data:
        import capo_bedrock.types.automated_reasoning_check_invalid_finding

        return {
            "invalid": capo_bedrock.types.automated_reasoning_check_invalid_finding.deserialize_json(
                data["invalid"]
            )
        }
    elif "satisfiable" in data:
        import capo_bedrock.types.automated_reasoning_check_satisfiable_finding

        return {
            "satisfiable": capo_bedrock.types.automated_reasoning_check_satisfiable_finding.deserialize_json(
                data["satisfiable"]
            )
        }
    elif "impossible" in data:
        import capo_bedrock.types.automated_reasoning_check_impossible_finding

        return {
            "impossible": capo_bedrock.types.automated_reasoning_check_impossible_finding.deserialize_json(
                data["impossible"]
            )
        }
    elif "translationAmbiguous" in data:
        import capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding

        return {
            "translationAmbiguous": capo_bedrock.types.automated_reasoning_check_translation_ambiguous_finding.deserialize_json(
                data["translationAmbiguous"]
            )
        }
    elif "tooComplex" in data:
        import capo_bedrock.types.automated_reasoning_check_too_complex_finding

        return {
            "tooComplex": capo_bedrock.types.automated_reasoning_check_too_complex_finding.deserialize_json(
                data["tooComplex"]
            )
        }
    elif "noTranslations" in data:
        import capo_bedrock.types.automated_reasoning_check_no_translations_finding

        return {
            "noTranslations": capo_bedrock.types.automated_reasoning_check_no_translations_finding.deserialize_json(
                data["noTranslations"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningCheckFinding: no recognized variant key"
        )
