"""Generated from Smithy shape ``com.amazonaws.devopsagent#SlackChannel``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError


class SlackChannel(TypedDict):
    channel_name: NotRequired["str"]
    """<p>Slack channel name</p>"""
    channel_id: "str"
    """<p>Slack channel ID</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackChannel) -> dict:
    out: dict = {}
    if "channel_name" in value:
        out["channelName"] = value["channel_name"]
    out["channelId"] = value["channel_id"]
    return out


def deserialize_json(data: dict) -> SlackChannel:
    out: SlackChannel = {}  # type: ignore[typeddict-item]
    if "channelName" in data:
        out["channel_name"] = data["channelName"]
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    else:
        raise DeserializationError("SlackChannel.channel_id required")
    return out
