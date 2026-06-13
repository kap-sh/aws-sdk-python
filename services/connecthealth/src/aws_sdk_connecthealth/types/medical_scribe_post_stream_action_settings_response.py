"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribePostStreamActionSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.clinical_note_generation_settings_response
    import aws_sdk_connecthealth.types.s3_uri


class MedicalScribePostStreamActionSettingsResponse(TypedDict):
    output_s3_uri: "aws_sdk_connecthealth.types.s3_uri.S3Uri"
    """<p/>"""
    clinical_note_generation_settings: "aws_sdk_connecthealth.types.clinical_note_generation_settings_response.ClinicalNoteGenerationSettingsResponse"
    """<p>Settings for clinical note generation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePostStreamActionSettingsResponse) -> dict:
    out: dict = {}
    out["outputS3Uri"] = value["output_s3_uri"]
    import aws_sdk_connecthealth.types.clinical_note_generation_settings_response

    out["clinicalNoteGenerationSettings"] = (
        aws_sdk_connecthealth.types.clinical_note_generation_settings_response.serialize_json(
            value["clinical_note_generation_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> MedicalScribePostStreamActionSettingsResponse:
    out: MedicalScribePostStreamActionSettingsResponse = {}  # type: ignore[typeddict-item]
    if "outputS3Uri" in data:
        out["output_s3_uri"] = data["outputS3Uri"]
    else:
        raise DeserializationError(
            "MedicalScribePostStreamActionSettingsResponse.output_s3_uri required"
        )
    if "clinicalNoteGenerationSettings" in data:
        import aws_sdk_connecthealth.types.clinical_note_generation_settings_response

        out["clinical_note_generation_settings"] = (
            aws_sdk_connecthealth.types.clinical_note_generation_settings_response.deserialize_json(
                data["clinicalNoteGenerationSettings"]
            )
        )
    else:
        raise DeserializationError(
            "MedicalScribePostStreamActionSettingsResponse.clinical_note_generation_settings required"
        )
    return out
