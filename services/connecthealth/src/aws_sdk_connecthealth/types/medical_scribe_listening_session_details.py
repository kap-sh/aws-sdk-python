"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeListeningSessionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_connecthealth.types.domain_id
    import aws_sdk_connecthealth.types.medical_scribe_channel_definitions
    import aws_sdk_connecthealth.types.medical_scribe_language_code
    import aws_sdk_connecthealth.types.medical_scribe_media_encoding
    import aws_sdk_connecthealth.types.medical_scribe_media_sample_rate_hertz
    import aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings_response
    import aws_sdk_connecthealth.types.medical_scribe_post_stream_actions_result
    import aws_sdk_connecthealth.types.medical_scribe_stream_status
    import aws_sdk_connecthealth.types.non_null_boolean
    import aws_sdk_connecthealth.types.scribe_session_id
    import aws_sdk_connecthealth.types.subscription_id


class MedicalScribeListeningSessionDetails(TypedDict):
    session_id: NotRequired[
        "aws_sdk_connecthealth.types.scribe_session_id.ScribeSessionId"
    ]
    """<p>The Session identifier</p>"""
    domain_id: NotRequired["aws_sdk_connecthealth.types.domain_id.DomainId"]
    """<p>The Domain identifier</p>"""
    subscription_id: NotRequired[
        "aws_sdk_connecthealth.types.subscription_id.SubscriptionId"
    ]
    """<p>The Subscription identifier</p>"""
    language_code: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_language_code.MedicalScribeLanguageCode"
    ]
    """<p>The Language Code for the audio in the session</p>"""
    media_sample_rate_hertz: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_media_sample_rate_hertz.MedicalScribeMediaSampleRateHertz"
    ]
    """<p>The sample rate of the input audio</p>"""
    media_encoding: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_media_encoding.MedicalScribeMediaEncoding"
    ]
    """<p>The encoding for the input audio</p>"""
    channel_definitions: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_channel_definitions.MedicalScribeChannelDefinitions"
    ]
    """<p>Channel definitions for the audio stream</p>"""
    post_stream_action_settings: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings_response.MedicalScribePostStreamActionSettingsResponse"
    ]
    """<p>Settings for post-stream actions</p>"""
    post_stream_action_result: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_post_stream_actions_result.MedicalScribePostStreamActionsResult"
    ]
    """<p>Results of post-stream actions</p>"""
    encounter_context_provided: NotRequired[
        "aws_sdk_connecthealth.types.non_null_boolean.NonNullBoolean"
    ]
    """<p>Indicates whether encounter context was provided</p>"""
    stream_status: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_stream_status.MedicalScribeStreamStatus"
    ]
    """<p>The current status of the stream</p>"""
    stream_creation_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when the stream was created</p>"""
    stream_end_time: NotRequired["datetime.datetime"]
    """<p>The timestamp when the stream ended</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeListeningSessionDetails) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "subscription_id" in value:
        out["subscriptionId"] = value["subscription_id"]
    if "language_code" in value:
        import aws_sdk_connecthealth.types.medical_scribe_language_code

        out["languageCode"] = (
            aws_sdk_connecthealth.types.medical_scribe_language_code.serialize_json(
                value["language_code"]
            )
        )
    if "media_sample_rate_hertz" in value:
        out["mediaSampleRateHertz"] = value["media_sample_rate_hertz"]
    if "media_encoding" in value:
        import aws_sdk_connecthealth.types.medical_scribe_media_encoding

        out["mediaEncoding"] = (
            aws_sdk_connecthealth.types.medical_scribe_media_encoding.serialize_json(
                value["media_encoding"]
            )
        )
    if "channel_definitions" in value:
        import aws_sdk_connecthealth.types.medical_scribe_channel_definitions

        out["channelDefinitions"] = (
            aws_sdk_connecthealth.types.medical_scribe_channel_definitions.serialize_json(
                value["channel_definitions"]
            )
        )
    if "post_stream_action_settings" in value:
        import aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings_response

        out["postStreamActionSettings"] = (
            aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings_response.serialize_json(
                value["post_stream_action_settings"]
            )
        )
    if "post_stream_action_result" in value:
        import aws_sdk_connecthealth.types.medical_scribe_post_stream_actions_result

        out["postStreamActionResult"] = (
            aws_sdk_connecthealth.types.medical_scribe_post_stream_actions_result.serialize_json(
                value["post_stream_action_result"]
            )
        )
    if "encounter_context_provided" in value:
        out["encounterContextProvided"] = value["encounter_context_provided"]
    if "stream_status" in value:
        import aws_sdk_connecthealth.types.medical_scribe_stream_status

        out["streamStatus"] = (
            aws_sdk_connecthealth.types.medical_scribe_stream_status.serialize_json(
                value["stream_status"]
            )
        )
    if "stream_creation_time" in value:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["streamCreationTime"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.serialize_json(
                value["stream_creation_time"]
            )
        )
    if "stream_end_time" in value:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["streamEndTime"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.serialize_json(
                value["stream_end_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeListeningSessionDetails:
    out: MedicalScribeListeningSessionDetails = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "subscriptionId" in data:
        out["subscription_id"] = data["subscriptionId"]
    if "languageCode" in data:
        import aws_sdk_connecthealth.types.medical_scribe_language_code

        out["language_code"] = (
            aws_sdk_connecthealth.types.medical_scribe_language_code.deserialize_json(
                data["languageCode"]
            )
        )
    if "mediaSampleRateHertz" in data:
        out["media_sample_rate_hertz"] = data["mediaSampleRateHertz"]
    if "mediaEncoding" in data:
        import aws_sdk_connecthealth.types.medical_scribe_media_encoding

        out["media_encoding"] = (
            aws_sdk_connecthealth.types.medical_scribe_media_encoding.deserialize_json(
                data["mediaEncoding"]
            )
        )
    if "channelDefinitions" in data:
        import aws_sdk_connecthealth.types.medical_scribe_channel_definitions

        out["channel_definitions"] = (
            aws_sdk_connecthealth.types.medical_scribe_channel_definitions.deserialize_json(
                data["channelDefinitions"]
            )
        )
    if "postStreamActionSettings" in data:
        import aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings_response

        out["post_stream_action_settings"] = (
            aws_sdk_connecthealth.types.medical_scribe_post_stream_action_settings_response.deserialize_json(
                data["postStreamActionSettings"]
            )
        )
    if "postStreamActionResult" in data:
        import aws_sdk_connecthealth.types.medical_scribe_post_stream_actions_result

        out["post_stream_action_result"] = (
            aws_sdk_connecthealth.types.medical_scribe_post_stream_actions_result.deserialize_json(
                data["postStreamActionResult"]
            )
        )
    if "encounterContextProvided" in data:
        out["encounter_context_provided"] = data["encounterContextProvided"]
    if "streamStatus" in data:
        import aws_sdk_connecthealth.types.medical_scribe_stream_status

        out["stream_status"] = (
            aws_sdk_connecthealth.types.medical_scribe_stream_status.deserialize_json(
                data["streamStatus"]
            )
        )
    if "streamCreationTime" in data:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["stream_creation_time"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.deserialize_json(
                data["streamCreationTime"]
            )
        )
    if "streamEndTime" in data:
        import aws_sdk_connecthealth.types._prelude.timestamp

        out["stream_end_time"] = (
            aws_sdk_connecthealth.types._prelude.timestamp.deserialize_json(
                data["streamEndTime"]
            )
        )
    return out
