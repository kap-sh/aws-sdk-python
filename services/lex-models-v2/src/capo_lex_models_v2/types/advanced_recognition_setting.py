"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#AdvancedRecognitionSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.audio_recognition_strategy


class AdvancedRecognitionSetting(TypedDict, closed=True):
    audio_recognition_strategy: NotRequired[
        "capo_lex_models_v2.types.audio_recognition_strategy.AudioRecognitionStrategy"
    ]
    """<p>Enables using the slot values as a custom vocabulary for recognizing user utterances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedRecognitionSetting) -> dict:
    out: dict = {}
    if "audio_recognition_strategy" in value:
        import capo_lex_models_v2.types.audio_recognition_strategy

        out["audioRecognitionStrategy"] = (
            capo_lex_models_v2.types.audio_recognition_strategy.serialize_json(
                value["audio_recognition_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> AdvancedRecognitionSetting:
    out: AdvancedRecognitionSetting = {}  # type: ignore[typeddict-item]
    if "audioRecognitionStrategy" in data:
        import capo_lex_models_v2.types.audio_recognition_strategy

        out["audio_recognition_strategy"] = (
            capo_lex_models_v2.types.audio_recognition_strategy.deserialize_json(
                data["audioRecognitionStrategy"]
            )
        )
    return out
