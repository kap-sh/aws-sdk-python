"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalTranscriptionJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.date_time
    import aws_sdk_transcribe.types.failure_reason
    import aws_sdk_transcribe.types.language_code
    import aws_sdk_transcribe.types.medical_content_identification_type
    import aws_sdk_transcribe.types.output_location_type
    import aws_sdk_transcribe.types.specialty
    import aws_sdk_transcribe.types.transcription_job_name
    import aws_sdk_transcribe.types.transcription_job_status
    import aws_sdk_transcribe.types.type


class MedicalTranscriptionJobSummary(TypedDict, closed=True):
    medical_transcription_job_name: NotRequired[
        "aws_sdk_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>The name of the medical transcription job. Job names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    creation_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified medical transcription job request was made.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    start_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time your medical transcription job began processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.789000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    completion_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified medical transcription job finished processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:33:13.922000-07:00</code> represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.</p>"""
    language_code: NotRequired["aws_sdk_transcribe.types.language_code.LanguageCode"]
    """<p>The language code used to create your medical transcription. US English (<code>en-US</code>) is the only supported language for medical transcriptions.</p>"""
    transcription_job_status: NotRequired[
        "aws_sdk_transcribe.types.transcription_job_status.TranscriptionJobStatus"
    ]
    """<p>Provides the status of your medical transcription job.</p> <p>If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>TranscriptFileUri</code>. If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p>"""
    failure_reason: NotRequired["aws_sdk_transcribe.types.failure_reason.FailureReason"]
    r"""<p>If <code>TranscriptionJobStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the transcription job failed. See also: <a href=\"https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html\">Common Errors</a>.</p>"""
    output_location_type: NotRequired[
        "aws_sdk_transcribe.types.output_location_type.OutputLocationType"
    ]
    """<p>Indicates where the specified medical transcription output is stored.</p> <p>If the value is <code>CUSTOMER_BUCKET</code>, the location is the Amazon S3 bucket you specified using the <code>OutputBucketName</code> parameter in your request. If you also included <code>OutputKey</code> in your request, your output is located in the path you specified in your request.</p> <p>If the value is <code>SERVICE_BUCKET</code>, the location is a service-managed Amazon S3 bucket. To access a transcript stored in a service-managed bucket, use the URI shown in the <code>TranscriptFileUri</code> field.</p>"""
    specialty: NotRequired["aws_sdk_transcribe.types.specialty.Specialty"]
    """<p>Provides the medical specialty represented in your media.</p>"""
    content_identification_type: NotRequired[
        "aws_sdk_transcribe.types.medical_content_identification_type.MedicalContentIdentificationType"
    ]
    r"""<p>Labels all personal health information (PHI) identified in your transcript. For more information, see <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/phi-id.html\">Identifying personal health information (PHI) in a transcription</a>.</p>"""
    type: NotRequired["aws_sdk_transcribe.types.type.Type"]
    """<p>Indicates whether the input media is a dictation or a conversation, as specified in the <code>StartMedicalTranscriptionJob</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalTranscriptionJobSummary) -> dict:
    out: dict = {}
    if "medical_transcription_job_name" in value:
        out["MedicalTranscriptionJobName"] = value["medical_transcription_job_name"]
    if "creation_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["CreationTime"] = aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "start_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["StartTime"] = aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "completion_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["CompletionTime"] = (
            aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
                value["completion_time"]
            )
        )
    if "language_code" in value:
        import aws_sdk_transcribe.types.language_code

        out["LanguageCode"] = (
            aws_sdk_transcribe.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "transcription_job_status" in value:
        import aws_sdk_transcribe.types.transcription_job_status

        out["TranscriptionJobStatus"] = (
            aws_sdk_transcribe.types.transcription_job_status.serialize_aws_json_1_1(
                value["transcription_job_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "output_location_type" in value:
        import aws_sdk_transcribe.types.output_location_type

        out["OutputLocationType"] = (
            aws_sdk_transcribe.types.output_location_type.serialize_aws_json_1_1(
                value["output_location_type"]
            )
        )
    if "specialty" in value:
        import aws_sdk_transcribe.types.specialty

        out["Specialty"] = aws_sdk_transcribe.types.specialty.serialize_aws_json_1_1(
            value["specialty"]
        )
    if "content_identification_type" in value:
        import aws_sdk_transcribe.types.medical_content_identification_type

        out["ContentIdentificationType"] = (
            aws_sdk_transcribe.types.medical_content_identification_type.serialize_aws_json_1_1(
                value["content_identification_type"]
            )
        )
    if "type" in value:
        import aws_sdk_transcribe.types.type

        out["Type"] = aws_sdk_transcribe.types.type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalTranscriptionJobSummary:
    out: MedicalTranscriptionJobSummary = {}  # type: ignore[typeddict-item]
    if "MedicalTranscriptionJobName" in data:
        out["medical_transcription_job_name"] = data["MedicalTranscriptionJobName"]
    if "CreationTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["creation_time"] = (
            aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["start_time"] = aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "CompletionTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["completion_time"] = (
            aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["CompletionTime"]
            )
        )
    if "LanguageCode" in data:
        import aws_sdk_transcribe.types.language_code

        out["language_code"] = (
            aws_sdk_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if "TranscriptionJobStatus" in data:
        import aws_sdk_transcribe.types.transcription_job_status

        out["transcription_job_status"] = (
            aws_sdk_transcribe.types.transcription_job_status.deserialize_aws_json_1_1(
                data["TranscriptionJobStatus"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "OutputLocationType" in data:
        import aws_sdk_transcribe.types.output_location_type

        out["output_location_type"] = (
            aws_sdk_transcribe.types.output_location_type.deserialize_aws_json_1_1(
                data["OutputLocationType"]
            )
        )
    if "Specialty" in data:
        import aws_sdk_transcribe.types.specialty

        out["specialty"] = aws_sdk_transcribe.types.specialty.deserialize_aws_json_1_1(
            data["Specialty"]
        )
    if "ContentIdentificationType" in data:
        import aws_sdk_transcribe.types.medical_content_identification_type

        out["content_identification_type"] = (
            aws_sdk_transcribe.types.medical_content_identification_type.deserialize_aws_json_1_1(
                data["ContentIdentificationType"]
            )
        )
    if "Type" in data:
        import aws_sdk_transcribe.types.type

        out["type"] = aws_sdk_transcribe.types.type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
