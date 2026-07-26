"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscriptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.engine_transcribe_medical_settings
    import capo_chime_sdk_meetings.types.engine_transcribe_settings


class TranscriptionConfiguration(TypedDict, closed=True):
    engine_transcribe_settings: NotRequired[
        "capo_chime_sdk_meetings.types.engine_transcribe_settings.EngineTranscribeSettings"
    ]
    """<p>The transcription configuration settings passed to Amazon Transcribe.</p>"""
    engine_transcribe_medical_settings: NotRequired[
        "capo_chime_sdk_meetings.types.engine_transcribe_medical_settings.EngineTranscribeMedicalSettings"
    ]
    """<p>The transcription configuration settings passed to Amazon Transcribe Medical.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptionConfiguration) -> dict:
    out: dict = {}
    if "engine_transcribe_settings" in value:
        import capo_chime_sdk_meetings.types.engine_transcribe_settings

        out["EngineTranscribeSettings"] = (
            capo_chime_sdk_meetings.types.engine_transcribe_settings.serialize_json(
                value["engine_transcribe_settings"]
            )
        )
    if "engine_transcribe_medical_settings" in value:
        import capo_chime_sdk_meetings.types.engine_transcribe_medical_settings

        out["EngineTranscribeMedicalSettings"] = (
            capo_chime_sdk_meetings.types.engine_transcribe_medical_settings.serialize_json(
                value["engine_transcribe_medical_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> TranscriptionConfiguration:
    out: TranscriptionConfiguration = {}  # type: ignore[typeddict-item]
    if "EngineTranscribeSettings" in data:
        import capo_chime_sdk_meetings.types.engine_transcribe_settings

        out["engine_transcribe_settings"] = (
            capo_chime_sdk_meetings.types.engine_transcribe_settings.deserialize_json(
                data["EngineTranscribeSettings"]
            )
        )
    if "EngineTranscribeMedicalSettings" in data:
        import capo_chime_sdk_meetings.types.engine_transcribe_medical_settings

        out["engine_transcribe_medical_settings"] = (
            capo_chime_sdk_meetings.types.engine_transcribe_medical_settings.deserialize_json(
                data["EngineTranscribeMedicalSettings"]
            )
        )
    return out
