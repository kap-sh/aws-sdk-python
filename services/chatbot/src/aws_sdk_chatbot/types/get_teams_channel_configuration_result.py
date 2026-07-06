"""Generated from Smithy shape ``com.amazonaws.chatbot#GetTeamsChannelConfigurationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.teams_channel_configuration


class GetTeamsChannelConfigurationResult(TypedDict, closed=True):
    channel_configuration: NotRequired[
        "aws_sdk_chatbot.types.teams_channel_configuration.TeamsChannelConfiguration"
    ]
    """<p>The configuration for a Microsoft Teams channel configured with AWS Chatbot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTeamsChannelConfigurationResult) -> dict:
    out: dict = {}
    if "channel_configuration" in value:
        import aws_sdk_chatbot.types.teams_channel_configuration

        out["ChannelConfiguration"] = (
            aws_sdk_chatbot.types.teams_channel_configuration.serialize_json(
                value["channel_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTeamsChannelConfigurationResult:
    out: GetTeamsChannelConfigurationResult = {}  # type: ignore[typeddict-item]
    if "ChannelConfiguration" in data:
        import aws_sdk_chatbot.types.teams_channel_configuration

        out["channel_configuration"] = (
            aws_sdk_chatbot.types.teams_channel_configuration.deserialize_json(
                data["ChannelConfiguration"]
            )
        )
    return out
