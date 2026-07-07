"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeConfigurationEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transcribe_streaming._protocol.eventstream import HeaderValue, Message
from aws_sdk_transcribe_streaming.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.iam_role_arn
    import aws_sdk_transcribe_streaming.types.medical_scribe_channel_definitions
    import aws_sdk_transcribe_streaming.types.medical_scribe_context
    import aws_sdk_transcribe_streaming.types.medical_scribe_encryption_settings
    import aws_sdk_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings
    import aws_sdk_transcribe_streaming.types.medical_scribe_vocabulary_filter_method
    import aws_sdk_transcribe_streaming.types.vocabulary_filter_name
    import aws_sdk_transcribe_streaming.types.vocabulary_name


class MedicalScribeConfigurationEvent(TypedDict, closed=True):
    vocabulary_name: NotRequired[
        "aws_sdk_transcribe_streaming.types.vocabulary_name.VocabularyName"
    ]
    """<p>Specify the name of the custom vocabulary you want to use for your streaming session. Custom vocabulary names are case-sensitive. </p>"""
    vocabulary_filter_name: NotRequired[
        "aws_sdk_transcribe_streaming.types.vocabulary_filter_name.VocabularyFilterName"
    ]
    """<p>Specify the name of the custom vocabulary filter you want to include in your streaming session. Custom vocabulary filter names are case-sensitive. </p> <p>If you include <code>VocabularyFilterName</code> in the <code>MedicalScribeConfigurationEvent</code>, you must also include <code>VocabularyFilterMethod</code>. </p>"""
    vocabulary_filter_method: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_vocabulary_filter_method.MedicalScribeVocabularyFilterMethod"
    ]
    """<p>Specify how you want your custom vocabulary filter applied to the streaming session.</p> <p>To replace words with <code>***</code>, specify <code>mask</code>. </p> <p>To delete words, specify <code>remove</code>. </p> <p>To flag words without changing them, specify <code>tag</code>. </p>"""
    resource_access_role_arn: (
        "aws_sdk_transcribe_streaming.types.iam_role_arn.IamRoleArn"
    )
    r"""<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 output bucket you specified, and use your KMS key if supplied. If the role that you specify doesn’t have the appropriate permissions, your request fails. </p> <p> IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/health-scribe-streaming.html\">Amazon Web Services HealthScribe</a>.</p>"""
    channel_definitions: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_channel_definitions.MedicalScribeChannelDefinitions"
    ]
    """<p>Specify which speaker is on which audio channel.</p>"""
    encryption_settings: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_encryption_settings.MedicalScribeEncryptionSettings"
    ]
    """<p>Specify the encryption settings for your streaming session.</p>"""
    post_stream_analytics_settings: "aws_sdk_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings.MedicalScribePostStreamAnalyticsSettings"
    """<p>Specify settings for post-stream analytics.</p>"""
    medical_scribe_context: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_context.MedicalScribeContext"
    ]
    """<p>The <code>MedicalScribeContext</code> object that contains contextual information used to generate customized clinical notes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeConfigurationEvent) -> dict:
    out: dict = {}
    if "vocabulary_name" in value:
        out["VocabularyName"] = value["vocabulary_name"]
    if "vocabulary_filter_name" in value:
        out["VocabularyFilterName"] = value["vocabulary_filter_name"]
    if "vocabulary_filter_method" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_vocabulary_filter_method

        out["VocabularyFilterMethod"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_vocabulary_filter_method.serialize_json(
                value["vocabulary_filter_method"]
            )
        )
    out["ResourceAccessRoleArn"] = value["resource_access_role_arn"]
    if "channel_definitions" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_channel_definitions

        out["ChannelDefinitions"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_channel_definitions.serialize_json(
                value["channel_definitions"]
            )
        )
    if "encryption_settings" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_encryption_settings

        out["EncryptionSettings"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_encryption_settings.serialize_json(
                value["encryption_settings"]
            )
        )
    import aws_sdk_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings

    out["PostStreamAnalyticsSettings"] = (
        aws_sdk_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings.serialize_json(
            value["post_stream_analytics_settings"]
        )
    )
    if "medical_scribe_context" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_context

        out["MedicalScribeContext"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_context.serialize_json(
                value["medical_scribe_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeConfigurationEvent:
    out: MedicalScribeConfigurationEvent = {}  # type: ignore[typeddict-item]
    if "VocabularyName" in data:
        out["vocabulary_name"] = data["VocabularyName"]
    if "VocabularyFilterName" in data:
        out["vocabulary_filter_name"] = data["VocabularyFilterName"]
    if "VocabularyFilterMethod" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_vocabulary_filter_method

        out["vocabulary_filter_method"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_vocabulary_filter_method.deserialize_json(
                data["VocabularyFilterMethod"]
            )
        )
    if "ResourceAccessRoleArn" in data:
        out["resource_access_role_arn"] = data["ResourceAccessRoleArn"]
    else:
        raise DeserializationError(
            "MedicalScribeConfigurationEvent.resource_access_role_arn required"
        )
    if "ChannelDefinitions" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_channel_definitions

        out["channel_definitions"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_channel_definitions.deserialize_json(
                data["ChannelDefinitions"]
            )
        )
    if "EncryptionSettings" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_encryption_settings

        out["encryption_settings"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_encryption_settings.deserialize_json(
                data["EncryptionSettings"]
            )
        )
    if "PostStreamAnalyticsSettings" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings

        out["post_stream_analytics_settings"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_post_stream_analytics_settings.deserialize_json(
                data["PostStreamAnalyticsSettings"]
            )
        )
    else:
        raise DeserializationError(
            "MedicalScribeConfigurationEvent.post_stream_analytics_settings required"
        )
    if "MedicalScribeContext" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_context

        out["medical_scribe_context"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_context.deserialize_json(
                data["MedicalScribeContext"]
            )
        )
    return out


def serialize_event_json(value: MedicalScribeConfigurationEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "ConfigurationEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> MedicalScribeConfigurationEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: MedicalScribeConfigurationEvent = {}  # type: ignore[typeddict-item]
    return out
