"""Generated from Smithy shape ``com.amazonaws.cloudtrail#UpdateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.channel_arn
    import aws_sdk_cloudtrail.types.channel_name
    import aws_sdk_cloudtrail.types.destinations


class UpdateChannelRequest(TypedDict, closed=True):
    channel: "aws_sdk_cloudtrail.types.channel_arn.ChannelArn"
    """<p>The ARN or ID (the ARN suffix) of the channel that you want to update.</p>"""
    destinations: NotRequired["aws_sdk_cloudtrail.types.destinations.Destinations"]
    """<p>The ARNs of event data stores that you want to log events arriving through the channel.</p>"""
    name: NotRequired["aws_sdk_cloudtrail.types.channel_name.ChannelName"]
    """<p> Changes the name of the channel. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateChannelRequest) -> dict:
    out: dict = {}
    out["Channel"] = value["channel"]
    if "destinations" in value:
        import aws_sdk_cloudtrail.types.destinations

        out["Destinations"] = (
            aws_sdk_cloudtrail.types.destinations.serialize_aws_json_1_1(
                value["destinations"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateChannelRequest:
    out: UpdateChannelRequest = {}  # type: ignore[typeddict-item]
    if "Channel" in data:
        out["channel"] = data["Channel"]
    else:
        raise DeserializationError("UpdateChannelRequest.channel required")
    if "Destinations" in data:
        import aws_sdk_cloudtrail.types.destinations

        out["destinations"] = (
            aws_sdk_cloudtrail.types.destinations.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    return out
