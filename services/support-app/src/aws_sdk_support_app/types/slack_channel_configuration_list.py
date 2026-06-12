"""Generated from Smithy shape ``com.amazonaws.supportapp#slackChannelConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support_app.types.slack_channel_configuration

slackChannelConfigurationList: TypeAlias = list[
    "aws_sdk_support_app.types.slack_channel_configuration.SlackChannelConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: slackChannelConfigurationList) -> list:
    import aws_sdk_support_app.types.slack_channel_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_support_app.types.slack_channel_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> slackChannelConfigurationList:
    import aws_sdk_support_app.types.slack_channel_configuration

    out: slackChannelConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_support_app.types.slack_channel_configuration.deserialize_json(item)
        )
    return out
