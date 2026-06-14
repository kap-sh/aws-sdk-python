"""Generated from Smithy shape ``com.amazonaws.transcribe#TranscriptionJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.boolean
    import aws_sdk_transcribe.types.content_redaction
    import aws_sdk_transcribe.types.date_time
    import aws_sdk_transcribe.types.failure_reason
    import aws_sdk_transcribe.types.identified_language_score
    import aws_sdk_transcribe.types.language_code
    import aws_sdk_transcribe.types.language_code_list
    import aws_sdk_transcribe.types.model_settings
    import aws_sdk_transcribe.types.output_location_type
    import aws_sdk_transcribe.types.toxicity_detection
    import aws_sdk_transcribe.types.transcription_job_name
    import aws_sdk_transcribe.types.transcription_job_status


class TranscriptionJobSummary(TypedDict):
    transcription_job_name: NotRequired[
        "aws_sdk_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>The name of the transcription job. Job names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    creation_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified transcription job request was made.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    start_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time your transcription job began processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.789000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    completion_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified transcription job finished processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:33:13.922000-07:00</code> represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.</p>"""
    language_code: NotRequired["aws_sdk_transcribe.types.language_code.LanguageCode"]
    """<p>The language code used to create your transcription.</p>"""
    transcription_job_status: NotRequired[
        "aws_sdk_transcribe.types.transcription_job_status.TranscriptionJobStatus"
    ]
    """<p>Provides the status of your transcription job.</p> <p>If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>TranscriptFileUri</code> (or <code>RedactedTranscriptFileUri</code>, if you requested transcript redaction). If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p>"""
    failure_reason: NotRequired["aws_sdk_transcribe.types.failure_reason.FailureReason"]
    r"""<p>If <code>TranscriptionJobStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the transcription job failed. See also: <a href=\"https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html\">Common Errors</a>.</p>"""
    output_location_type: NotRequired[
        "aws_sdk_transcribe.types.output_location_type.OutputLocationType"
    ]
    """<p>Indicates where the specified transcription output is stored.</p> <p>If the value is <code>CUSTOMER_BUCKET</code>, the location is the Amazon S3 bucket you specified using the <code>OutputBucketName</code> parameter in your request. If you also included <code>OutputKey</code> in your request, your output is located in the path you specified in your request.</p> <p>If the value is <code>SERVICE_BUCKET</code>, the location is a service-managed Amazon S3 bucket. To access a transcript stored in a service-managed bucket, use the URI shown in the <code>TranscriptFileUri</code> or <code>RedactedTranscriptFileUri</code> field.</p>"""
    content_redaction: NotRequired[
        "aws_sdk_transcribe.types.content_redaction.ContentRedaction"
    ]
    """<p>The content redaction settings of the transcription job.</p>"""
    model_settings: NotRequired["aws_sdk_transcribe.types.model_settings.ModelSettings"]
    identify_language: NotRequired["aws_sdk_transcribe.types.boolean.Boolean"]
    """<p>Indicates whether automatic language identification was enabled (<code>TRUE</code>) for the specified transcription job.</p>"""
    identify_multiple_languages: NotRequired["aws_sdk_transcribe.types.boolean.Boolean"]
    """<p>Indicates whether automatic multi-language identification was enabled (<code>TRUE</code>) for the specified transcription job.</p>"""
    identified_language_score: NotRequired[
        "aws_sdk_transcribe.types.identified_language_score.IdentifiedLanguageScore"
    ]
    """<p>The confidence score associated with the language identified in your media file.</p> <p>Confidence scores are values between 0 and 1; a larger value indicates a higher probability that the identified language correctly matches the language spoken in your media.</p>"""
    language_codes: NotRequired[
        "aws_sdk_transcribe.types.language_code_list.LanguageCodeList"
    ]
    """<p>The language codes used to create your transcription job. This parameter is used with multi-language identification. For single-language identification, the singular version of this parameter, <code>LanguageCode</code>, is present.</p>"""
    toxicity_detection: NotRequired[
        "aws_sdk_transcribe.types.toxicity_detection.ToxicityDetection"
    ]
    """<p>Indicates whether toxicity detection was enabled for the specified transcription job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranscriptionJobSummary) -> dict:
    out: dict = {}
    if "transcription_job_name" in value:
        out["TranscriptionJobName"] = value["transcription_job_name"]
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
    if "content_redaction" in value:
        import aws_sdk_transcribe.types.content_redaction

        out["ContentRedaction"] = (
            aws_sdk_transcribe.types.content_redaction.serialize_aws_json_1_1(
                value["content_redaction"]
            )
        )
    if "model_settings" in value:
        import aws_sdk_transcribe.types.model_settings

        out["ModelSettings"] = (
            aws_sdk_transcribe.types.model_settings.serialize_aws_json_1_1(
                value["model_settings"]
            )
        )
    if "identify_language" in value:
        out["IdentifyLanguage"] = value["identify_language"]
    if "identify_multiple_languages" in value:
        out["IdentifyMultipleLanguages"] = value["identify_multiple_languages"]
    if "identified_language_score" in value:
        out["IdentifiedLanguageScore"] = value["identified_language_score"]
    if "language_codes" in value:
        import aws_sdk_transcribe.types.language_code_list

        out["LanguageCodes"] = (
            aws_sdk_transcribe.types.language_code_list.serialize_aws_json_1_1(
                value["language_codes"]
            )
        )
    if "toxicity_detection" in value:
        import aws_sdk_transcribe.types.toxicity_detection

        out["ToxicityDetection"] = (
            aws_sdk_transcribe.types.toxicity_detection.serialize_aws_json_1_1(
                value["toxicity_detection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TranscriptionJobSummary:
    out: TranscriptionJobSummary = {}  # type: ignore[typeddict-item]
    if "TranscriptionJobName" in data:
        out["transcription_job_name"] = data["TranscriptionJobName"]
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
    if "ContentRedaction" in data:
        import aws_sdk_transcribe.types.content_redaction

        out["content_redaction"] = (
            aws_sdk_transcribe.types.content_redaction.deserialize_aws_json_1_1(
                data["ContentRedaction"]
            )
        )
    if "ModelSettings" in data:
        import aws_sdk_transcribe.types.model_settings

        out["model_settings"] = (
            aws_sdk_transcribe.types.model_settings.deserialize_aws_json_1_1(
                data["ModelSettings"]
            )
        )
    if "IdentifyLanguage" in data:
        out["identify_language"] = data["IdentifyLanguage"]
    if "IdentifyMultipleLanguages" in data:
        out["identify_multiple_languages"] = data["IdentifyMultipleLanguages"]
    if "IdentifiedLanguageScore" in data:
        out["identified_language_score"] = data["IdentifiedLanguageScore"]
    if "LanguageCodes" in data:
        import aws_sdk_transcribe.types.language_code_list

        out["language_codes"] = (
            aws_sdk_transcribe.types.language_code_list.deserialize_aws_json_1_1(
                data["LanguageCodes"]
            )
        )
    if "ToxicityDetection" in data:
        import aws_sdk_transcribe.types.toxicity_detection

        out["toxicity_detection"] = (
            aws_sdk_transcribe.types.toxicity_detection.deserialize_aws_json_1_1(
                data["ToxicityDetection"]
            )
        )
    return out
