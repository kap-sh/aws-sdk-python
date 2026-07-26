"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribePostStreamAnalyticsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transcribe_streaming.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.clinical_note_generation_settings


class MedicalScribePostStreamAnalyticsSettings(TypedDict, closed=True):
    clinical_note_generation_settings: "capo_transcribe_streaming.types.clinical_note_generation_settings.ClinicalNoteGenerationSettings"
    """<p>Specify settings for the post-stream clinical note generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePostStreamAnalyticsSettings) -> dict:
    out: dict = {}
    import capo_transcribe_streaming.types.clinical_note_generation_settings

    out["ClinicalNoteGenerationSettings"] = (
        capo_transcribe_streaming.types.clinical_note_generation_settings.serialize_json(
            value["clinical_note_generation_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> MedicalScribePostStreamAnalyticsSettings:
    out: MedicalScribePostStreamAnalyticsSettings = {}  # type: ignore[typeddict-item]
    if "ClinicalNoteGenerationSettings" in data:
        import capo_transcribe_streaming.types.clinical_note_generation_settings

        out["clinical_note_generation_settings"] = (
            capo_transcribe_streaming.types.clinical_note_generation_settings.deserialize_json(
                data["ClinicalNoteGenerationSettings"]
            )
        )
    else:
        raise DeserializationError(
            "MedicalScribePostStreamAnalyticsSettings.clinical_note_generation_settings required"
        )
    return out
