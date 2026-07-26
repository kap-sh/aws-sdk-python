"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Channel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.channel_arn
    import capo_cloudtrail.types.channel_name


class Channel(TypedDict, closed=True):
    channel_arn: NotRequired["capo_cloudtrail.types.channel_arn.ChannelArn"]
    """<p>The Amazon Resource Name (ARN) of a channel.</p>"""
    name: NotRequired["capo_cloudtrail.types.channel_name.ChannelName"]
    """<p> The name of the CloudTrail channel. For service-linked channels, the name is <code>aws-service-channel/service-name/custom-suffix</code> where <code>service-name</code> represents the name of the Amazon Web Services service that created the channel and <code>custom-suffix</code> represents the suffix created by the Amazon Web Services service. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Channel) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Channel:
    out: Channel = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
