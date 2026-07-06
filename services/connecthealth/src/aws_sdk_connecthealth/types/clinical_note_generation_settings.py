"""Generated from Smithy shape ``com.amazonaws.connecthealth#ClinicalNoteGenerationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.note_template_settings


class ClinicalNoteGenerationSettings(TypedDict, closed=True):
    note_template_settings: (
        "aws_sdk_connecthealth.types.note_template_settings.NoteTemplateSettings"
    )
    """<p>Settings for the note template to use</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClinicalNoteGenerationSettings) -> dict:
    out: dict = {}
    import aws_sdk_connecthealth.types.note_template_settings

    out["noteTemplateSettings"] = (
        aws_sdk_connecthealth.types.note_template_settings.serialize_json(
            value["note_template_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> ClinicalNoteGenerationSettings:
    out: ClinicalNoteGenerationSettings = {}  # type: ignore[typeddict-item]
    if "noteTemplateSettings" in data:
        import aws_sdk_connecthealth.types.note_template_settings

        out["note_template_settings"] = (
            aws_sdk_connecthealth.types.note_template_settings.deserialize_json(
                data["noteTemplateSettings"]
            )
        )
    else:
        raise DeserializationError(
            "ClinicalNoteGenerationSettings.note_template_settings required"
        )
    return out
