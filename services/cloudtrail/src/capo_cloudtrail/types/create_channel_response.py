"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CreateChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.channel_arn
    import capo_cloudtrail.types.channel_name
    import capo_cloudtrail.types.destinations
    import capo_cloudtrail.types.source
    import capo_cloudtrail.types.tags_list


class CreateChannelResponse(TypedDict, closed=True):
    channel_arn: NotRequired["capo_cloudtrail.types.channel_arn.ChannelArn"]
    """<p>The Amazon Resource Name (ARN) of the new channel.</p>"""
    name: NotRequired["capo_cloudtrail.types.channel_name.ChannelName"]
    """<p>The name of the new channel.</p>"""
    source: NotRequired["capo_cloudtrail.types.source.Source"]
    """<p>The partner or external event source name.</p>"""
    destinations: NotRequired["capo_cloudtrail.types.destinations.Destinations"]
    """<p>The event data stores that log the events arriving through the channel.</p>"""
    tags: NotRequired["capo_cloudtrail.types.tags_list.TagsList"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateChannelResponse) -> dict:
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
    if "tags" in value:
        import capo_cloudtrail.types.tags_list

        out["Tags"] = capo_cloudtrail.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateChannelResponse:
    out: CreateChannelResponse = {}  # type: ignore[typeddict-item]
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
    if "Tags" in data:
        import capo_cloudtrail.types.tags_list

        out["tags"] = capo_cloudtrail.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
