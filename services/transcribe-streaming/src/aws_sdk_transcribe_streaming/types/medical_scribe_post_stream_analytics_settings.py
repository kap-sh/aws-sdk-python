"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribePostStreamAnalyticsSettings``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transcribe_streaming.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.clinical_note_generation_settings


class MedicalScribePostStreamAnalyticsSettings(TypedDict):
    clinical_note_generation_settings: "aws_sdk_transcribe_streaming.types.clinical_note_generation_settings.ClinicalNoteGenerationSettings"
    """<p>Specify settings for the post-stream clinical note generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePostStreamAnalyticsSettings) -> dict:
    out: dict = {}
    import aws_sdk_transcribe_streaming.types.clinical_note_generation_settings

    out["ClinicalNoteGenerationSettings"] = (
        aws_sdk_transcribe_streaming.types.clinical_note_generation_settings.serialize_json(
            value["clinical_note_generation_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> MedicalScribePostStreamAnalyticsSettings:
    out: MedicalScribePostStreamAnalyticsSettings = {}  # type: ignore[typeddict-item]
    if "ClinicalNoteGenerationSettings" in data:
        import aws_sdk_transcribe_streaming.types.clinical_note_generation_settings

        out["clinical_note_generation_settings"] = (
            aws_sdk_transcribe_streaming.types.clinical_note_generation_settings.deserialize_json(
                data["ClinicalNoteGenerationSettings"]
            )
        )
    else:
        raise DeserializationError(
            "MedicalScribePostStreamAnalyticsSettings.clinical_note_generation_settings required"
        )
    return out
