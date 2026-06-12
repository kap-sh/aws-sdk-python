"""Generated from Smithy shape ``com.amazonaws.chatbot#CreateSlackChannelConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.slack_channel_configuration


class CreateSlackChannelConfigurationResult(TypedDict):
    channel_configuration: NotRequired[
        "aws_sdk_chatbot.types.slack_channel_configuration.SlackChannelConfiguration"
    ]
    """<p>The configuration for a Slack channel configured with AWS Chatbot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSlackChannelConfigurationResult) -> dict:
    out: dict = {}
    if "channel_configuration" in value:
        import aws_sdk_chatbot.types.slack_channel_configuration

        out["ChannelConfiguration"] = (
            aws_sdk_chatbot.types.slack_channel_configuration.serialize_json(
                value["channel_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSlackChannelConfigurationResult:
    out: CreateSlackChannelConfigurationResult = {}  # type: ignore[typeddict-item]
    if "ChannelConfiguration" in data:
        import aws_sdk_chatbot.types.slack_channel_configuration

        out["channel_configuration"] = (
            aws_sdk_chatbot.types.slack_channel_configuration.deserialize_json(
                data["ChannelConfiguration"]
            )
        )
    return out
