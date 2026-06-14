"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsJob``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.call_analytics_job_details
    import aws_sdk_transcribe.types.call_analytics_job_name
    import aws_sdk_transcribe.types.call_analytics_job_settings
    import aws_sdk_transcribe.types.call_analytics_job_status
    import aws_sdk_transcribe.types.channel_definitions
    import aws_sdk_transcribe.types.data_access_role_arn
    import aws_sdk_transcribe.types.date_time
    import aws_sdk_transcribe.types.failure_reason
    import aws_sdk_transcribe.types.identified_language_score
    import aws_sdk_transcribe.types.language_code
    import aws_sdk_transcribe.types.media
    import aws_sdk_transcribe.types.media_format
    import aws_sdk_transcribe.types.media_sample_rate_hertz
    import aws_sdk_transcribe.types.tag_list
    import aws_sdk_transcribe.types.transcript


class CallAnalyticsJob(TypedDict):
    call_analytics_job_name: NotRequired[
        "aws_sdk_transcribe.types.call_analytics_job_name.CallAnalyticsJobName"
    ]
    """<p>The name of the Call Analytics job. Job names are case sensitive and must be unique within an Amazon Web Services account.</p>"""
    call_analytics_job_status: NotRequired[
        "aws_sdk_transcribe.types.call_analytics_job_status.CallAnalyticsJobStatus"
    ]
    """<p>Provides the status of the specified Call Analytics job.</p> <p>If the status is <code>COMPLETED</code>, the job is finished and you can find the results at the location specified in <code>TranscriptFileUri</code> (or <code>RedactedTranscriptFileUri</code>, if you requested transcript redaction). If the status is <code>FAILED</code>, <code>FailureReason</code> provides details on why your transcription job failed.</p>"""
    call_analytics_job_details: NotRequired[
        "aws_sdk_transcribe.types.call_analytics_job_details.CallAnalyticsJobDetails"
    ]
    """<p>Provides detailed information about a call analytics job, including information about skipped analytics features.</p>"""
    language_code: NotRequired["aws_sdk_transcribe.types.language_code.LanguageCode"]
    r"""<p>The language code used to create your Call Analytics job. For a list of supported languages and their associated language codes, refer to the <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html\">Supported languages</a> table.</p> <p>If you do not know the language spoken in your media file, you can omit this field and let Amazon Transcribe automatically identify the language of your media. To improve the accuracy of language identification, you can include several language codes and Amazon Transcribe chooses the closest match for your transcription.</p>"""
    media_sample_rate_hertz: NotRequired[
        "aws_sdk_transcribe.types.media_sample_rate_hertz.MediaSampleRateHertz"
    ]
    """<p>The sample rate, in hertz, of the audio track in your input media file.</p>"""
    media_format: NotRequired["aws_sdk_transcribe.types.media_format.MediaFormat"]
    """<p>The format of the input media file.</p>"""
    media: NotRequired["aws_sdk_transcribe.types.media.Media"]
    """<p>Provides the Amazon S3 location of the media file you used in your Call Analytics request.</p>"""
    transcript: NotRequired["aws_sdk_transcribe.types.transcript.Transcript"]
    start_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Call Analytics job began processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.789000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    creation_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Call Analytics job request was made.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents a transcription job that started processing at 12:32 PM UTC-7 on May 4, 2022.</p>"""
    completion_time: NotRequired["aws_sdk_transcribe.types.date_time.DateTime"]
    """<p>The date and time the specified Call Analytics job finished processing.</p> <p>Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:33:13.922000-07:00</code> represents a transcription job that started processing at 12:33 PM UTC-7 on May 4, 2022.</p>"""
    failure_reason: NotRequired["aws_sdk_transcribe.types.failure_reason.FailureReason"]
    r"""<p>If <code>CallAnalyticsJobStatus</code> is <code>FAILED</code>, <code>FailureReason</code> contains information about why the Call Analytics job request failed.</p> <p>The <code>FailureReason</code> field contains one of the following values:</p> <ul> <li> <p> <code>Unsupported media format</code>.</p> <p>The media format specified in <code>MediaFormat</code> isn't valid. Refer to refer to the <code>MediaFormat</code> parameter for a list of supported formats.</p> </li> <li> <p> <code>The media format provided does not match the detected media format</code>.</p> <p>The media format specified in <code>MediaFormat</code> doesn't match the format of the input file. Check the media format of your media file and correct the specified value.</p> </li> <li> <p> <code>Invalid sample rate for audio file</code>.</p> <p>The sample rate specified in <code>MediaSampleRateHertz</code> isn't valid. The sample rate must be between 8,000 and 48,000 hertz.</p> </li> <li> <p> <code>The sample rate provided does not match the detected sample rate</code>.</p> <p>The sample rate specified in <code>MediaSampleRateHertz</code> doesn't match the sample rate detected in your input media file. Check the sample rate of your media file and correct the specified value.</p> </li> <li> <p> <code>Invalid file size: file size too large</code>.</p> <p>The size of your media file is larger than what Amazon Transcribe can process. For more information, refer to <a href=\"https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe\">Service quotas</a>.</p> </li> <li> <p> <code>Invalid number of channels: number of channels too large</code>.</p> <p>Your audio contains more channels than Amazon Transcribe is able to process. For more information, refer to <a href=\"https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe\">Service quotas</a>.</p> </li> </ul>"""
    data_access_role_arn: NotRequired[
        "aws_sdk_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) you included in your request.</p>"""
    identified_language_score: NotRequired[
        "aws_sdk_transcribe.types.identified_language_score.IdentifiedLanguageScore"
    ]
    """<p>The confidence score associated with the language identified in your media file.</p> <p>Confidence scores are values between 0 and 1; a larger value indicates a higher probability that the identified language correctly matches the language spoken in your media.</p>"""
    settings: NotRequired[
        "aws_sdk_transcribe.types.call_analytics_job_settings.CallAnalyticsJobSettings"
    ]
    """<p>Provides information on any additional settings that were included in your request. Additional settings include content redaction and language identification settings.</p>"""
    channel_definitions: NotRequired[
        "aws_sdk_transcribe.types.channel_definitions.ChannelDefinitions"
    ]
    """<p>Indicates which speaker is on which channel.</p>"""
    tags: NotRequired["aws_sdk_transcribe.types.tag_list.TagList"]
    """<p>The tags, each in the form of a key:value pair, assigned to the specified call analytics job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsJob) -> dict:
    out: dict = {}
    if "call_analytics_job_name" in value:
        out["CallAnalyticsJobName"] = value["call_analytics_job_name"]
    if "call_analytics_job_status" in value:
        import aws_sdk_transcribe.types.call_analytics_job_status

        out["CallAnalyticsJobStatus"] = (
            aws_sdk_transcribe.types.call_analytics_job_status.serialize_aws_json_1_1(
                value["call_analytics_job_status"]
            )
        )
    if "call_analytics_job_details" in value:
        import aws_sdk_transcribe.types.call_analytics_job_details

        out["CallAnalyticsJobDetails"] = (
            aws_sdk_transcribe.types.call_analytics_job_details.serialize_aws_json_1_1(
                value["call_analytics_job_details"]
            )
        )
    if "language_code" in value:
        import aws_sdk_transcribe.types.language_code

        out["LanguageCode"] = (
            aws_sdk_transcribe.types.language_code.serialize_aws_json_1_1(
                value["language_code"]
            )
        )
    if "media_sample_rate_hertz" in value:
        out["MediaSampleRateHertz"] = value["media_sample_rate_hertz"]
    if "media_format" in value:
        import aws_sdk_transcribe.types.media_format

        out["MediaFormat"] = (
            aws_sdk_transcribe.types.media_format.serialize_aws_json_1_1(
                value["media_format"]
            )
        )
    if "media" in value:
        import aws_sdk_transcribe.types.media

        out["Media"] = aws_sdk_transcribe.types.media.serialize_aws_json_1_1(
            value["media"]
        )
    if "transcript" in value:
        import aws_sdk_transcribe.types.transcript

        out["Transcript"] = aws_sdk_transcribe.types.transcript.serialize_aws_json_1_1(
            value["transcript"]
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
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    if "identified_language_score" in value:
        out["IdentifiedLanguageScore"] = value["identified_language_score"]
    if "settings" in value:
        import aws_sdk_transcribe.types.call_analytics_job_settings

        out["Settings"] = (
            aws_sdk_transcribe.types.call_analytics_job_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    if "channel_definitions" in value:
        import aws_sdk_transcribe.types.channel_definitions

        out["ChannelDefinitions"] = (
            aws_sdk_transcribe.types.channel_definitions.serialize_aws_json_1_1(
                value["channel_definitions"]
            )
        )
    if "tags" in value:
        import aws_sdk_transcribe.types.tag_list

        out["Tags"] = aws_sdk_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CallAnalyticsJob:
    out: CallAnalyticsJob = {}  # type: ignore[typeddict-item]
    if "CallAnalyticsJobName" in data:
        out["call_analytics_job_name"] = data["CallAnalyticsJobName"]
    if "CallAnalyticsJobStatus" in data:
        import aws_sdk_transcribe.types.call_analytics_job_status

        out["call_analytics_job_status"] = (
            aws_sdk_transcribe.types.call_analytics_job_status.deserialize_aws_json_1_1(
                data["CallAnalyticsJobStatus"]
            )
        )
    if "CallAnalyticsJobDetails" in data:
        import aws_sdk_transcribe.types.call_analytics_job_details

        out["call_analytics_job_details"] = (
            aws_sdk_transcribe.types.call_analytics_job_details.deserialize_aws_json_1_1(
                data["CallAnalyticsJobDetails"]
            )
        )
    if "LanguageCode" in data:
        import aws_sdk_transcribe.types.language_code

        out["language_code"] = (
            aws_sdk_transcribe.types.language_code.deserialize_aws_json_1_1(
                data["LanguageCode"]
            )
        )
    if "MediaSampleRateHertz" in data:
        out["media_sample_rate_hertz"] = data["MediaSampleRateHertz"]
    if "MediaFormat" in data:
        import aws_sdk_transcribe.types.media_format

        out["media_format"] = (
            aws_sdk_transcribe.types.media_format.deserialize_aws_json_1_1(
                data["MediaFormat"]
            )
        )
    if "Media" in data:
        import aws_sdk_transcribe.types.media

        out["media"] = aws_sdk_transcribe.types.media.deserialize_aws_json_1_1(
            data["Media"]
        )
    if "Transcript" in data:
        import aws_sdk_transcribe.types.transcript

        out["transcript"] = (
            aws_sdk_transcribe.types.transcript.deserialize_aws_json_1_1(
                data["Transcript"]
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
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    if "IdentifiedLanguageScore" in data:
        out["identified_language_score"] = data["IdentifiedLanguageScore"]
    if "Settings" in data:
        import aws_sdk_transcribe.types.call_analytics_job_settings

        out["settings"] = (
            aws_sdk_transcribe.types.call_analytics_job_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    if "ChannelDefinitions" in data:
        import aws_sdk_transcribe.types.channel_definitions

        out["channel_definitions"] = (
            aws_sdk_transcribe.types.channel_definitions.deserialize_aws_json_1_1(
                data["ChannelDefinitions"]
            )
        )
    if "Tags" in data:
        import aws_sdk_transcribe.types.tag_list

        out["tags"] = aws_sdk_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
