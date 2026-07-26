"""Generated from Smithy shape ``com.amazonaws.connecthealth#ClinicalNoteGenerationSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.note_template_settings_response


class ClinicalNoteGenerationSettingsResponse(TypedDict, closed=True):
    note_template_settings: NotRequired[
        "capo_connecthealth.types.note_template_settings_response.NoteTemplateSettingsResponse"
    ]
    """<p>Settings for the note template used</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClinicalNoteGenerationSettingsResponse) -> dict:
    out: dict = {}
    if "note_template_settings" in value:
        import capo_connecthealth.types.note_template_settings_response

        out["noteTemplateSettings"] = (
            capo_connecthealth.types.note_template_settings_response.serialize_json(
                value["note_template_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClinicalNoteGenerationSettingsResponse:
    out: ClinicalNoteGenerationSettingsResponse = {}  # type: ignore[typeddict-item]
    if "noteTemplateSettings" in data:
        import capo_connecthealth.types.note_template_settings_response

        out["note_template_settings"] = (
            capo_connecthealth.types.note_template_settings_response.deserialize_json(
                data["noteTemplateSettings"]
            )
        )
    return out
