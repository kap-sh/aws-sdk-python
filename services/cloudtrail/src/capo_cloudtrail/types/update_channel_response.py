"""Generated from Smithy shape ``com.amazonaws.cloudtrail#UpdateChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.channel_arn
    import capo_cloudtrail.types.channel_name
    import capo_cloudtrail.types.destinations
    import capo_cloudtrail.types.source


class UpdateChannelResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_cloudtrail.types.channel_arn.ChannelArn"]
    """<p>The ARN of the channel that was updated.</p>"""
    name: NotRequired["capo_cloudtrail.types.channel_name.ChannelName"]
    """<p>The name of the channel that was updated.</p>"""
    source: NotRequired["capo_cloudtrail.types.source.Source"]
    """<p>The event source of the channel that was updated.</p>"""
    destinations: NotRequired["capo_cloudtrail.types.destinations.Destinations"]
    """<p>The event data stores that log events arriving through the channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateChannelResponse) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelArn"] = value["channel_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "source" in value:
        out["Source"] = value["source"]
    if "destinations" in value:
        import capo_cloudtrail.types.destinations

        out["Destinations"] = capo_cloudtrail.types.destinations.serialize_aws_json_1_1(
            value["destinations"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateChannelResponse:
    out: UpdateChannelResponse = {}  # type: ignore[typeddict-item]
    if "ChannelArn" in data:
        out["channel_arn"] = data["ChannelArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Source" in data:
        out["source"] = data["Source"]
    if "Destinations" in data:
        import capo_cloudtrail.types.destinations

        out["destinations"] = (
            capo_cloudtrail.types.destinations.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    return out
