"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribePostStreamActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.clinical_note_generation_settings
    import aws_sdk_connecthealth.types.s3_uri


class MedicalScribePostStreamActionSettings(TypedDict, closed=True):
    output_s3_uri: "aws_sdk_connecthealth.types.s3_uri.S3Uri"
    """<p/>"""
    clinical_note_generation_settings: "aws_sdk_connecthealth.types.clinical_note_generation_settings.ClinicalNoteGenerationSettings"
    """<p>Settings for clinical note generation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePostStreamActionSettings) -> dict:
    out: dict = {}
    out["outputS3Uri"] = value["output_s3_uri"]
    import aws_sdk_connecthealth.types.clinical_note_generation_settings

    out["clinicalNoteGenerationSettings"] = (
        aws_sdk_connecthealth.types.clinical_note_generation_settings.serialize_json(
            value["clinical_note_generation_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> MedicalScribePostStreamActionSettings:
    out: MedicalScribePostStreamActionSettings = {}  # type: ignore[typeddict-item]
    if "outputS3Uri" in data:
        out["output_s3_uri"] = data["outputS3Uri"]
    else:
        raise DeserializationError(
            "MedicalScribePostStreamActionSettings.output_s3_uri required"
        )
    if "clinicalNoteGenerationSettings" in data:
        import aws_sdk_connecthealth.types.clinical_note_generation_settings

        out["clinical_note_generation_settings"] = (
            aws_sdk_connecthealth.types.clinical_note_generation_settings.deserialize_json(
                data["clinicalNoteGenerationSettings"]
            )
        )
    else:
        raise DeserializationError(
            "MedicalScribePostStreamActionSettings.clinical_note_generation_settings required"
        )
    return out
