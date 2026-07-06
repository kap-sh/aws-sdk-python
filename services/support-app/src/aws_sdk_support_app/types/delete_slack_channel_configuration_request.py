"""Generated from Smithy shape ``com.amazonaws.supportapp#DeleteSlackChannelConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_support_app.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_support_app.types.channel_id
    import aws_sdk_support_app.types.team_id


class DeleteSlackChannelConfigurationRequest(TypedDict, closed=True):
    team_id: "aws_sdk_support_app.types.team_id.teamId"
    """<p>The team ID in Slack. This ID uniquely identifies a Slack workspace, such as <code>T012ABCDEFG</code>.</p>"""
    channel_id: "aws_sdk_support_app.types.channel_id.channelId"
    """<p>The channel ID in Slack. This ID identifies a channel within a Slack workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSlackChannelConfigurationRequest) -> dict:
    out: dict = {}
    out["teamId"] = value["team_id"]
    out["channelId"] = value["channel_id"]
    return out


def deserialize_json(data: dict) -> DeleteSlackChannelConfigurationRequest:
    out: DeleteSlackChannelConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "teamId" in data:
        out["team_id"] = data["teamId"]
    else:
        raise DeserializationError(
            "DeleteSlackChannelConfigurationRequest.team_id required"
        )
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    else:
        raise DeserializationError(
            "DeleteSlackChannelConfigurationRequest.channel_id required"
        )
    return out
