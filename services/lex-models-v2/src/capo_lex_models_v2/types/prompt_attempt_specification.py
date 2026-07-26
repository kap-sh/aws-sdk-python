"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#PromptAttemptSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.allowed_input_types
    import capo_lex_models_v2.types.audio_and_dtmf_input_specification
    import capo_lex_models_v2.types.boxed_boolean
    import capo_lex_models_v2.types.text_input_specification


class PromptAttemptSpecification(TypedDict, closed=True):
    allow_interrupt: NotRequired["capo_lex_models_v2.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether the user can interrupt a speech prompt attempt from the bot.</p>"""
    allowed_input_types: (
        "capo_lex_models_v2.types.allowed_input_types.AllowedInputTypes"
    )
    """<p>Indicates the allowed input types of the prompt attempt.</p>"""
    audio_and_dtmf_input_specification: NotRequired[
        "capo_lex_models_v2.types.audio_and_dtmf_input_specification.AudioAndDTMFInputSpecification"
    ]
    """<p>Specifies the settings on audio and DTMF input.</p>"""
    text_input_specification: NotRequired[
        "capo_lex_models_v2.types.text_input_specification.TextInputSpecification"
    ]
    """<p>Specifies the settings on text input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptAttemptSpecification) -> dict:
    out: dict = {}
    if "allow_interrupt" in value:
        out["allowInterrupt"] = value["allow_interrupt"]
    import capo_lex_models_v2.types.allowed_input_types

    out["allowedInputTypes"] = (
        capo_lex_models_v2.types.allowed_input_types.serialize_json(
            value["allowed_input_types"]
        )
    )
    if "audio_and_dtmf_input_specification" in value:
        import capo_lex_models_v2.types.audio_and_dtmf_input_specification

        out["audioAndDTMFInputSpecification"] = (
            capo_lex_models_v2.types.audio_and_dtmf_input_specification.serialize_json(
                value["audio_and_dtmf_input_specification"]
            )
        )
    if "text_input_specification" in value:
        import capo_lex_models_v2.types.text_input_specification

        out["textInputSpecification"] = (
            capo_lex_models_v2.types.text_input_specification.serialize_json(
                value["text_input_specification"]
            )
        )
    return out


def deserialize_json(data: dict) -> PromptAttemptSpecification:
    out: PromptAttemptSpecification = {}  # type: ignore[typeddict-item]
    if "allowInterrupt" in data:
        out["allow_interrupt"] = data["allowInterrupt"]
    if "allowedInputTypes" in data:
        import capo_lex_models_v2.types.allowed_input_types

        out["allowed_input_types"] = (
            capo_lex_models_v2.types.allowed_input_types.deserialize_json(
                data["allowedInputTypes"]
            )
        )
    else:
        raise DeserializationError(
            "PromptAttemptSpecification.allowed_input_types required"
        )
    if "audioAndDTMFInputSpecification" in data:
        import capo_lex_models_v2.types.audio_and_dtmf_input_specification

        out["audio_and_dtmf_input_specification"] = (
            capo_lex_models_v2.types.audio_and_dtmf_input_specification.deserialize_json(
                data["audioAndDTMFInputSpecification"]
            )
        )
    if "textInputSpecification" in data:
        import capo_lex_models_v2.types.text_input_specification

        out["text_input_specification"] = (
            capo_lex_models_v2.types.text_input_specification.deserialize_json(
                data["textInputSpecification"]
            )
        )
    return out
