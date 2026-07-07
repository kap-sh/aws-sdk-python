"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.boolean
    import aws_sdk_transcribe.types.data_access_role_arn
    import aws_sdk_transcribe.types.date_time
    import aws_sdk_transcribe.types.failure_reason
    import aws_sdk_transcribe.types.media
    import aws_sdk_transcribe.types.medical_scribe_channel_definitions
    import aws_sdk_transcribe.types.medical_scribe_job_status
    import aws_sdk_transcribe.types.medical_scribe_language_code
    import aws_sdk_transcribe.types.medical_scribe_output
    import aws_sdk_transcribe.types.medical_scribe_settings
    import aws_sdk_transcribe.types.tag_list
    import aws_sdk_transcribe.types.transcription_job_name


class MedicalScribeJob(TypedDict, closed=True):
    medical_scribe_job_name: NotRequired[
        "aws_sdk_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>The name of the Medical Scribe job. Job names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    medical_scribe_job_status: NotRequired[
        "aws_sdk_transcribe.types.medical_scribe_job_status.MedicalScribeJobStatus"
    ]
    """<p>Provides the status of the specified Medical Scribe job.</p> <p>If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>MedicalScribeOutput</code> If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your Medical Scribe job failed.</p>"""
    language_code: NotRequired[
        "aws_sdk_transcribe.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    ]
    """<p>The language code used to create your Medical Scribe job. US English (<code>en-US</code>) is the only supported language for Medical Scribe jobs. </p>"""
    media: NotRequired["aws_sdk_transcribe.types.media.Media"]
    medical_scribe_output: NotRequired[
        "aws_sdk_transcribe.types.medical_scribe_output.MedicalScribeOutput"
    ]
    """<p>The location of the output of your Medical Scribe job. <code>ClinicalDocumentUri</code> holds the Amazon S3 URI for the Clinical Document and <code>TranscriptFileUri</code> holds the Amazon S3 URI for the Transcript.</p>"""
    start_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time your Medical Scribe job began processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.789000-07:00</code> represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    creation_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Medical Scribe job request was made.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    completion_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Medical Scribe job finished processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a Medical Scribe job that finished processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    failure_reason: NotRequired["aws_sdk_transcribe.types.failure_reason.FailureReason"]
    r"""<p>If <code>MedicalScribeJobStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the transcription job failed. See also: <a href=\"https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html\">Common Errors</a>.</p>"""
    settings: NotRequired[
        "aws_sdk_transcribe.types.medical_scribe_settings.MedicalScribeSettings"
    ]
    """<p>Makes it possible to control how your Medical Scribe job is processed using a <code>MedicalScribeSettings</code> object. Specify <code>ChannelIdentification</code> if <code>ChannelDefinitions</code> are set. Enabled <code>ShowSpeakerLabels</code> if <code>ChannelIdentification</code> and <code>ChannelDefinitions</code> are not set. One and only one of <code>ChannelIdentification</code> and <code>ShowSpeakerLabels</code> must be set. If <code>ShowSpeakerLabels</code> is set, <code>MaxSpeakerLabels</code> must also be set. Use <code>Settings</code> to specify a vocabulary or vocabulary filter or both using <code>VocabularyName</code>, <code>VocabularyFilterName</code>. <code>VocabularyFilterMethod</code> must be specified if <code>VocabularyFilterName</code> is set. </p>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files, write to the output bucket, and use your KMS key if supplied. If the role that you specify doesn’t have the appropriate permissions your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns\">IAM ARNs</a>.</p>"""
    channel_definitions: NotRequired[
        "aws_sdk_transcribe.types.medical_scribe_channel_definitions.MedicalScribeChannelDefinitions"
    ]
    """<p>Makes it possible to specify which speaker is on which channel. For example, if the clinician is the first participant to speak, you would set <code>ChannelId</code> of the first <code>ChannelDefinition</code> in the list to <code>0</code> (to indicate the first channel) and <code>ParticipantRole</code> to <code>CLINICIAN</code> (to indicate that it's the clinician speaking). Then you would set the <code>ChannelId</code> of the second <code>ChannelDefinition</code> in the list to <code>1</code> (to indicate the second channel) and <code>ParticipantRole</code> to <code>PATIENT</code> (to indicate that it's the patient speaking). </p>"""
    medical_scribe_context_provided: NotRequired[
        "aws_sdk_transcribe.types.boolean.Boolean"
    ]
    """<p>Indicates whether the <code>MedicalScribeContext</code> object was provided when the Medical Scribe job was started.</p>"""
    tags: NotRequired["aws_sdk_transcribe.types.tag_list.TagList"]
    r"""<p>Adds one or more custom tags, each in the form of a key:value pair, to the Medical Scribe job.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html\">Tagging resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeJob) -> dict:
    out: dict = {}
    if "medical_scribe_job_name" in value:
        out["MedicalScribeJobName"] = value["medical_scribe_job_name"]
    if "medical_scribe_job_status" in value:
        import aws_sdk_transcribe.types.medical_scribe_job_status

        out["MedicalScribeJobStatus"] = (
            aws_sdk_transcribe.types.medical_scribe_job_status.serialize_aws_json_1_1(
                value["medical_scribe_job_status"]
            )
        )
    if "language_code" in value:
        import aws_sdk_transcribe.types.medical_scribe_language_code

        out["LanguageCode"] = (
            aws_sdk_transcribe.types.medical_scribe_language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "media" in value:
        import aws_sdk_transcribe.types.media

        out["Media"] = aws_sdk_transcribe.types.media.serialize_aws_json_1_1(
            value["media"]
        )
    if "medical_scribe_output" in value:
        import aws_sdk_transcribe.types.medical_scribe_output

        out["MedicalScribeOutput"] = (
            aws_sdk_transcribe.types.medical_scribe_output.serialize_aws_json_1_1(
                value["medical_scribe_output"]
            )
        )
    if "start_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["StartTime"] = aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "creation_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["CreationTime"] = aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "completion_time" in value:
        import aws_sdk_transcribe.types.date_time

        out["CompletionTime"] = (
            aws_sdk_transcribe.types.date_time.serialize_aws_json_1_1(
                value["completion_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "settings" in value:
        import aws_sdk_transcribe.types.medical_scribe_settings

        out["Settings"] = (
            aws_sdk_transcribe.types.medical_scribe_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "channel_definitions" in value:
        import aws_sdk_transcribe.types.medical_scribe_channel_definitions

        out["ChannelDefinitions"] = (
            aws_sdk_transcribe.types.medical_scribe_channel_definitions.serialize_aws_json_1_1(
                value["channel_definitions"]
            )
        )
    if "medical_scribe_context_provided" in value:
        out["MedicalScribeContextProvided"] = value["medical_scribe_context_provided"]
    if "tags" in value:
        import aws_sdk_transcribe.types.tag_list

        out["Tags"] = aws_sdk_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalScribeJob:
    out: MedicalScribeJob = {}  # type: ignore[typeddict-item]
    if "MedicalScribeJobName" in data:
        out["medical_scribe_job_name"] = data["MedicalScribeJobName"]
    if "MedicalScribeJobStatus" in data:
        import aws_sdk_transcribe.types.medical_scribe_job_status

        out["medical_scribe_job_status"] = (
            aws_sdk_transcribe.types.medical_scribe_job_status.deserialize_aws_json_1_1(
                data["MedicalScribeJobStatus"]
            )
        )
    if "LanguageCode" in data:
        import aws_sdk_transcribe.types.medical_scribe_language_code

        out["language_code"] = (
            aws_sdk_transcribe.types.medical_scribe_language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if "Media" in data:
        import aws_sdk_transcribe.types.media

        out["media"] = aws_sdk_transcribe.types.media.deserialize_aws_json_1_1(
            data["Media"]
        )
    if "MedicalScribeOutput" in data:
        import aws_sdk_transcribe.types.medical_scribe_output

        out["medical_scribe_output"] = (
            aws_sdk_transcribe.types.medical_scribe_output.deserialize_aws_json_1_1(
                data["MedicalScribeOutput"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["start_time"] = aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "CreationTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["creation_time"] = (
            aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "CompletionTime" in data:
        import aws_sdk_transcribe.types.date_time

        out["completion_time"] = (
            aws_sdk_transcribe.types.date_time.deserialize_aws_json_1_1(
                data["CompletionTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "Settings" in data:
        import aws_sdk_transcribe.types.medical_scribe_settings

        out["settings"] = (
            aws_sdk_transcribe.types.medical_scribe_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "ChannelDefinitions" in data:
        import aws_sdk_transcribe.types.medical_scribe_channel_definitions

        out["channel_definitions"] = (
            aws_sdk_transcribe.types.medical_scribe_channel_definitions.deserialize_aws_json_1_1(
                data["ChannelDefinitions"]
            )
        )
    if "MedicalScribeContextProvided" in data:
        out["medical_scribe_context_provided"] = data["MedicalScribeContextProvided"]
    if "Tags" in data:
        import aws_sdk_transcribe.types.tag_list

        out["tags"] = aws_sdk_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
