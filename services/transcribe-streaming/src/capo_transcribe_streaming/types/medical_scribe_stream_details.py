"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeStreamDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.date_time
    import capo_transcribe_streaming.types.iam_role_arn
    import capo_transcribe_streaming.types.medical_scribe_channel_definitions
    import capo_transcribe_streaming.types.medical_scribe_encryption_settings
    import capo_transcribe_streaming.types.medical_scribe_language_code
    import capo_transcribe_streaming.types.medical_scribe_media_encoding
    import capo_transcribe_streaming.types.medical_scribe_media_sample_rate_hertz
    import capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_result
    import capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings
    import capo_transcribe_streaming.types.medical_scribe_stream_status
    import capo_transcribe_streaming.types.medical_scribe_vocabulary_filter_method
    import capo_transcribe_streaming.types.nullable_boolean
    import capo_transcribe_streaming.types.session_id
    import capo_transcribe_streaming.types.vocabulary_filter_name
    import capo_transcribe_streaming.types.vocabulary_name


class MedicalScribeStreamDetails(TypedDict, closed=True):
    session_id: NotRequired["capo_transcribe_streaming.types.session_id.SessionId"]
    """<p>The identifier of the HealthScribe streaming session.</p>"""
    stream_created_at: NotRequired["capo_transcribe_streaming.types.date_time.DateTime"]
    """<p>The date and time when the HealthScribe streaming session was created.</p>"""
    stream_ended_at: NotRequired["capo_transcribe_streaming.types.date_time.DateTime"]
    """<p>The date and time when the HealthScribe streaming session was ended.</p>"""
    language_code: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    ]
    """<p>The Language Code of the HealthScribe streaming session.</p>"""
    media_sample_rate_hertz: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz"
    ]
    """<p>The sample rate (in hertz) of the HealthScribe streaming session.</p>"""
    media_encoding: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding"
    ]
    """<p>The Media Encoding of the HealthScribe streaming session.</p>"""
    vocabulary_name: NotRequired[
        "capo_transcribe_streaming.types.vocabulary_name.VocabularyName"
    ]
    """<p>The vocabulary name of the HealthScribe streaming session.</p>"""
    vocabulary_filter_name: NotRequired[
        "capo_transcribe_streaming.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>The name of the vocabulary filter used for the HealthScribe streaming session .</p>"""
    vocabulary_filter_method: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_vocabulary_filter_method.MedicalScribeVocabularyFilterMethod"
    ]
    """<p>The method of the vocabulary filter for the HealthScribe streaming session.</p>"""
    resource_access_role_arn: NotRequired[
        "capo_transcribe_streaming.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the role used in the HealthScribe streaming session.</p>"""
    channel_definitions: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_channel_definitions.MedicalScribeChannelDefinitions"
    ]
    """<p>The Channel Definitions of the HealthScribe streaming session.</p>"""
    encryption_settings: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_encryption_settings.MedicalScribeEncryptionSettings"
    ]
    """<p>The Encryption Settings of the HealthScribe streaming session.</p>"""
    stream_status: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_stream_status.MedicalScribeStreamStatus"
    ]
    """<p>The streaming status of the HealthScribe streaming session.</p> <p>Possible Values:</p> <ul> <li> <p> <code>IN_PROGRESS</code> </p> </li> <li> <p> <code>PAUSED</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> <li> <p> <code>COMPLETED</code> </p> </li> </ul> <note> <p>This status is specific to real-time streaming. A <code>COMPLETED</code> status doesn't mean that the post-stream analytics is complete. To get status of an analytics result, check the <code>Status</code> field for the analytics result within the <code>MedicalScribePostStreamAnalyticsResult</code>. For example, you can view the status of the <code>ClinicalNoteGenerationResult</code>. </p> </note>"""
    post_stream_analytics_settings: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings.MedicalScribePostStreamAnalyticsSettings"
    ]
    """<p>The post-stream analytics settings of the HealthScribe streaming session.</p>"""
    post_stream_analytics_result: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_result.MedicalScribePostStreamAnalyticsResult"
    ]
    """<p>The result of post-stream analytics for the HealthScribe streaming session.</p>"""
    medical_scribe_context_provided: NotRequired[
        "capo_transcribe_streaming.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether the <code>MedicalScribeContext</code> object was provided when the stream was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeStreamDetails) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "stream_created_at" in value:
        import capo_transcribe_streaming.types.date_time

        out["StreamCreatedAt"] = (
            capo_transcribe_streaming.types.date_time.serialize_json(
                value["stream_created_at"]
            )
        )
    if "stream_ended_at" in value:
        import capo_transcribe_streaming.types.date_time

        out["StreamEndedAt"] = capo_transcribe_streaming.types.date_time.serialize_json(
            value["stream_ended_at"]
        )
    if "language_code" in value:
        import capo_transcribe_streaming.types.medical_scribe_language_code

        out["LanguageCode"] = (
            capo_transcribe_streaming.types.medical_scribe_language_code.serialize_json(
                value["language_code"]
            )
        )
    if "media_sample_rate_hertz" in value:
        out["MediaSampleRateHertz"] = value["media_sample_rate_hertz"]
    if "media_encoding" in value:
        import capo_transcribe_streaming.types.medical_scribe_media_encoding

        out["MediaEncoding"] = (
            capo_transcribe_streaming.types.medical_scribe_media_encoding.serialize_json(
                value["media_encoding"]
            )
        )
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    if "vocabulary_filter_method" in value:
        import capo_transcribe_streaming.types.medical_scribe_vocabulary_filter_method

        out["VocabularyFilterMethod"] = (
            capo_transcribe_streaming.types.medical_scribe_vocabulary_filter_method.serialize_json(
                value["vocabulary_filter_method"]
            )
        )
    if "resource_access_role_arn" in value:
        out["ResourceAccessRoleArn"] = value["resource_access_role_arn"]
    if "channel_definitions" in value:
        import capo_transcribe_streaming.types.medical_scribe_channel_definitions

        out["ChannelDefinitions"] = (
            capo_transcribe_streaming.types.medical_scribe_channel_definitions.serialize_json(
                value["channel_definitions"]
            )
        )
    if "encryption_settings" in value:
        import capo_transcribe_streaming.types.medical_scribe_encryption_settings

        out["EncryptionSettings"] = (
            capo_transcribe_streaming.types.medical_scribe_encryption_settings.serialize_json(
                value["encryption_settings"]
            )
        )
    if "stream_status" in value:
        import capo_transcribe_streaming.types.medical_scribe_stream_status

        out["StreamStatus"] = (
            capo_transcribe_streaming.types.medical_scribe_stream_status.serialize_json(
                value["stream_status"]
            )
        )
    if "post_stream_analytics_settings" in value:
        import capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings

        out["PostStreamAnalyticsSettings"] = (
            capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings.serialize_json(
                value["post_stream_analytics_settings"]
            )
        )
    if "post_stream_analytics_result" in value:
        import capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_result

        out["PostStreamAnalyticsResult"] = (
            capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_result.serialize_json(
                value["post_stream_analytics_result"]
            )
        )
    if "medical_scribe_context_provided" in value:
        out["MedicalScribeContextProvided"] = value["medical_scribe_context_provided"]
    return out


def deserialize_json(data: dict) -> MedicalScribeStreamDetails:
    out: MedicalScribeStreamDetails = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    if "StreamCreatedAt" in data:
        import capo_transcribe_streaming.types.date_time

        out["stream_created_at"] = (
            capo_transcribe_streaming.types.date_time.deserialize_json(
                data["StreamCreatedAt"]
            )
        )
    if "StreamEndedAt" in data:
        import capo_transcribe_streaming.types.date_time

        out["stream_ended_at"] = (
            capo_transcribe_streaming.types.date_time.deserialize_json(
                data["StreamEndedAt"]
            )
        )
    if "LanguageCode" in data:
        import capo_transcribe_streaming.types.medical_scribe_language_code

        out["language_code"] = (
            capo_transcribe_streaming.types.medical_scribe_language_code.deserialize_json(
                data["LanguageCode"]
            )
        )
    if "MediaSampleRateHertz" in data:
        out["media_sample_rate_hertz"] = data["MediaSampleRateHertz"]
    if "MediaEncoding" in data:
        import capo_transcribe_streaming.types.medical_scribe_media_encoding

        out["media_encoding"] = (
            capo_transcribe_streaming.types.medical_scribe_media_encoding.deserialize_json(
                data["MediaEncoding"]
            )
        )
    if "VocabularyName" in data:
        out["vocabulary_name"] = data["VocabularyName"]
    if "VocabularyFilterName" in data:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    if "VocabularyFilterMethod" in data:
        import capo_transcribe_streaming.types.medical_scribe_vocabulary_filter_method

        out["vocabulary_filter_method"] = (
            capo_transcribe_streaming.types.medical_scribe_vocabulary_filter_method.deserialize_json(
                data["VocabularyFilterMethod"]
            )
        )
    if "ResourceAccessRoleArn" in data:
        out["resource_access_role_arn"] = data["ResourceAccessRoleArn"]
    if "ChannelDefinitions" in data:
        import capo_transcribe_streaming.types.medical_scribe_channel_definitions

        out["channel_definitions"] = (
            capo_transcribe_streaming.types.medical_scribe_channel_definitions.deserialize_json(
                data["ChannelDefinitions"]
            )
        )
    if "EncryptionSettings" in data:
        import capo_transcribe_streaming.types.medical_scribe_encryption_settings

        out["encryption_settings"] = (
            capo_transcribe_streaming.types.medical_scribe_encryption_settings.deserialize_json(
                data["EncryptionSettings"]
            )
        )
    if "StreamStatus" in data:
        import capo_transcribe_streaming.types.medical_scribe_stream_status

        out["stream_status"] = (
            capo_transcribe_streaming.types.medical_scribe_stream_status.deserialize_json(
                data["StreamStatus"]
            )
        )
    if "PostStreamAnalyticsSettings" in data:
        import capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings

        out["post_stream_analytics_settings"] = (
            capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings.deserialize_json(
                data["PostStreamAnalyticsSettings"]
            )
        )
    if "PostStreamAnalyticsResult" in data:
        import capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_result

        out["post_stream_analytics_result"] = (
            capo_transcribe_streaming.types.medical_scribe_post_stream_analytics_result.deserialize_json(
                data["PostStreamAnalyticsResult"]
            )
        )
    if "MedicalScribeContextProvided" in data:
        out["medical_scribe_context_provided"] = data["MedicalScribeContextProvided"]
    return out
