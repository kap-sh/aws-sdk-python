"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#UtteranceInputSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.test_set_utterance_text
    import aws_sdk_lex_models_v2.types.utterance_audio_input_specification


class UtteranceInputSpecification(TypedDict):
    text_input: NotRequired[
        "aws_sdk_lex_models_v2.types.test_set_utterance_text.TestSetUtteranceText"
    ]
    """<p>A text input transcription of the utterance. It is only applicable for test-sets containing text data.</p>"""
    audio_input: NotRequired[
        "aws_sdk_lex_models_v2.types.utterance_audio_input_specification.UtteranceAudioInputSpecification"
    ]
    """<p>Contains information about the audio input for an utterance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceInputSpecification) -> dict:
    out: dict = {}
    if "text_input" in value:
        out["textInput"] = value["text_input"]
    if "audio_input" in value:
        import aws_sdk_lex_models_v2.types.utterance_audio_input_specification

        out["audioInput"] = (
            aws_sdk_lex_models_v2.types.utterance_audio_input_specification.serialize_json(
                value["audio_input"]
            )
        )
    return out


def deserialize_json(data: dict) -> UtteranceInputSpecification:
    out: UtteranceInputSpecification = {}  # type: ignore[typeddict-item]
    if "textInput" in data:
        out["text_input"] = data["textInput"]
    if "audioInput" in data:
        import aws_sdk_lex_models_v2.types.utterance_audio_input_specification

        out["audio_input"] = (
            aws_sdk_lex_models_v2.types.utterance_audio_input_specification.deserialize_json(
                data["audioInput"]
            )
        )
    return out
