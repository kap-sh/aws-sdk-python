"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ConfigurationEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.channel_definitions
    import aws_sdk_transcribe_streaming.types.post_call_analytics_settings


class ConfigurationEvent(TypedDict):
    channel_definitions: NotRequired[
        "aws_sdk_transcribe_streaming.types.channel_definitions.ChannelDefinitions"
    ]
    """<p>Indicates which speaker is on which audio channel.</p>"""
    post_call_analytics_settings: NotRequired[
        "aws_sdk_transcribe_streaming.types.post_call_analytics_settings.PostCallAnalyticsSettings"
    ]
    """<p>Provides additional optional settings for your Call Analytics post-call request, including encryption and output locations for your redacted transcript.</p> <p> <code>PostCallAnalyticsSettings</code> provides you with the same insights as a Call Analytics post-call transcription. Refer to <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/tca-post-call.html\">Post-call analytics</a> for more information on this feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationEvent) -> dict:
    out: dict = {}
    if "channel_definitions" in value:
        import aws_sdk_transcribe_streaming.types.channel_definitions

        out["ChannelDefinitions"] = (
            aws_sdk_transcribe_streaming.types.channel_definitions.serialize_json(
                value["channel_definitions"]
            )
        )
    if "post_call_analytics_settings" in value:
        import aws_sdk_transcribe_streaming.types.post_call_analytics_settings

        out["PostCallAnalyticsSettings"] = (
            aws_sdk_transcribe_streaming.types.post_call_analytics_settings.serialize_json(
                value["post_call_analytics_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationEvent:
    out: ConfigurationEvent = {}  # type: ignore[typeddict-item]
    if "ChannelDefinitions" in data:
        import aws_sdk_transcribe_streaming.types.channel_definitions

        out["channel_definitions"] = (
            aws_sdk_transcribe_streaming.types.channel_definitions.deserialize_json(
                data["ChannelDefinitions"]
            )
        )
    if "PostCallAnalyticsSettings" in data:
        import aws_sdk_transcribe_streaming.types.post_call_analytics_settings

        out["post_call_analytics_settings"] = (
            aws_sdk_transcribe_streaming.types.post_call_analytics_settings.deserialize_json(
                data["PostCallAnalyticsSettings"]
            )
        )
    return out
