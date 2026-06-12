"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#TranscriptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.engine_transcribe_medical_settings
    import aws_sdk_chime_sdk_meetings.types.engine_transcribe_settings


class TranscriptionConfiguration(TypedDict):
    engine_transcribe_settings: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.engine_transcribe_settings.EngineTranscribeSettings"
    ]
    """<p>The transcription configuration settings passed to Amazon Transcribe.</p>"""
    engine_transcribe_medical_settings: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.engine_transcribe_medical_settings.EngineTranscribeMedicalSettings"
    ]
    """<p>The transcription configuration settings passed to Amazon Transcribe Medical.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptionConfiguration) -> dict:
    out: dict = {}
    if "engine_transcribe_settings" in value:
        import aws_sdk_chime_sdk_meetings.types.engine_transcribe_settings

        out["EngineTranscribeSettings"] = (
            aws_sdk_chime_sdk_meetings.types.engine_transcribe_settings.serialize_json(
                value["engine_transcribe_settings"]
            )
        )
    if "engine_transcribe_medical_settings" in value:
        import aws_sdk_chime_sdk_meetings.types.engine_transcribe_medical_settings

        out["EngineTranscribeMedicalSettings"] = (
            aws_sdk_chime_sdk_meetings.types.engine_transcribe_medical_settings.serialize_json(
                value["engine_transcribe_medical_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> TranscriptionConfiguration:
    out: TranscriptionConfiguration = {}  # type: ignore[typeddict-item]
    if "EngineTranscribeSettings" in data:
        import aws_sdk_chime_sdk_meetings.types.engine_transcribe_settings

        out["engine_transcribe_settings"] = (
            aws_sdk_chime_sdk_meetings.types.engine_transcribe_settings.deserialize_json(
                data["EngineTranscribeSettings"]
            )
        )
    if "EngineTranscribeMedicalSettings" in data:
        import aws_sdk_chime_sdk_meetings.types.engine_transcribe_medical_settings

        out["engine_transcribe_medical_settings"] = (
            aws_sdk_chime_sdk_meetings.types.engine_transcribe_medical_settings.deserialize_json(
                data["EngineTranscribeMedicalSettings"]
            )
        )
    return out
