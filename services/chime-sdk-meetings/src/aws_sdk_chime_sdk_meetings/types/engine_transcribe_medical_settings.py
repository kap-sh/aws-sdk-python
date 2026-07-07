"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#EngineTranscribeMedicalSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.string
    import aws_sdk_chime_sdk_meetings.types.transcribe_medical_content_identification_type
    import aws_sdk_chime_sdk_meetings.types.transcribe_medical_language_code
    import aws_sdk_chime_sdk_meetings.types.transcribe_medical_region
    import aws_sdk_chime_sdk_meetings.types.transcribe_medical_specialty
    import aws_sdk_chime_sdk_meetings.types.transcribe_medical_type


class EngineTranscribeMedicalSettings(TypedDict, closed=True):
    language_code: "aws_sdk_chime_sdk_meetings.types.transcribe_medical_language_code.TranscribeMedicalLanguageCode"
    """<p>The language code specified for the Amazon Transcribe Medical engine.</p>"""
    specialty: "aws_sdk_chime_sdk_meetings.types.transcribe_medical_specialty.TranscribeMedicalSpecialty"
    """<p>The specialty specified for the Amazon Transcribe Medical engine.</p>"""
    type: (
        "aws_sdk_chime_sdk_meetings.types.transcribe_medical_type.TranscribeMedicalType"
    )
    """<p>The type of transcription.</p>"""
    vocabulary_name: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    """<p>The name of the vocabulary passed to Amazon Transcribe Medical.</p>"""
    region: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_medical_region.TranscribeMedicalRegion"
    ]
    """<p>The Amazon Web Services Region passed to Amazon Transcribe Medical. If you don't specify a Region, Amazon Chime uses the meeting's Region. </p>"""
    content_identification_type: NotRequired[
        "aws_sdk_chime_sdk_meetings.types.transcribe_medical_content_identification_type.TranscribeMedicalContentIdentificationType"
    ]
    """<p>Set this field to <code>PHI</code> to identify personal health information in the transcription output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EngineTranscribeMedicalSettings) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_meetings.types.transcribe_medical_language_code

    out["LanguageCode"] = (
        aws_sdk_chime_sdk_meetings.types.transcribe_medical_language_code.serialize_json(
            value["language_code"]
        )
    )
    import aws_sdk_chime_sdk_meetings.types.transcribe_medical_specialty

    out["Specialty"] = (
        aws_sdk_chime_sdk_meetings.types.transcribe_medical_specialty.serialize_json(
            value["specialty"]
        )
    )
    import aws_sdk_chime_sdk_meetings.types.transcribe_medical_type

    out["Type"] = (
        aws_sdk_chime_sdk_meetings.types.transcribe_medical_type.serialize_json(
            value["type"]
        )
    )
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "region" in value:
        import aws_sdk_chime_sdk_meetings.types.transcribe_medical_region

        out["Region"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_medical_region.serialize_json(
                value["region"]
            )
        )
    if "content_identification_type" in value:
        import aws_sdk_chime_sdk_meetings.types.transcribe_medical_content_identification_type

        out["ContentIdentificationType"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_medical_content_identification_type.serialize_json(
                value["content_identification_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> EngineTranscribeMedicalSettings:
    out: EngineTranscribeMedicalSettings = {}  # type: ignore[typeddict-item]
    if "LanguageCode" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_medical_language_code

        out["language_code"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_medical_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    else:
        raise DeserializationError(
            "EngineTranscribeMedicalSettings.language_code required"
        )
    if "Specialty" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_medical_specialty

        out["specialty"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_medical_specialty.deserialize_json(
                data["Specialty"]
            )
        )
    else:
        raise DeserializationError("EngineTranscribeMedicalSettings.specialty required")
    if "Type" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_medical_type

        out["type"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_medical_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("EngineTranscribeMedicalSettings.type required")
    if "VocabularyName" in data:
        out["vocabulary_name"] = data["VocabularyName"]
    if "Region" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_medical_region

        out["region"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_medical_region.deserialize_json(
                data["Region"]
            )
        )
    if "ContentIdentificationType" in data:
        import aws_sdk_chime_sdk_meetings.types.transcribe_medical_content_identification_type

        out["content_identification_type"] = (
            aws_sdk_chime_sdk_meetings.types.transcribe_medical_content_identification_type.deserialize_json(
                data["ContentIdentificationType"]
            )
        )
    return out
