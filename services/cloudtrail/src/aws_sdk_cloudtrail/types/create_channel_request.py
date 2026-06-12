"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CreateChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.channel_name
    import aws_sdk_cloudtrail.types.destinations
    import aws_sdk_cloudtrail.types.source
    import aws_sdk_cloudtrail.types.tags_list


class CreateChannelRequest(TypedDict):
    name: "aws_sdk_cloudtrail.types.channel_name.ChannelName"
    """<p>The name of the channel.</p>"""
    source: "aws_sdk_cloudtrail.types.source.Source"
    """<p>The name of the partner or external event source. You cannot change this name after you create the channel. A maximum of one channel is allowed per source.</p> <p> A source can be either <code>Custom</code> for all valid non-Amazon Web Services events, or the name of a partner event source. For information about the source names for available partners, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-integration.html#cloudtrail-lake-partner-information\">Additional information about integration partners</a> in the CloudTrail User Guide. </p>"""
    destinations: "aws_sdk_cloudtrail.types.destinations.Destinations"
    """<p>One or more event data stores to which events arriving through a channel will be logged.</p>"""
    tags: NotRequired["aws_sdk_cloudtrail.types.tags_list.TagsList"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateChannelRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Source"] = value["source"]
    import aws_sdk_cloudtrail.types.destinations

    out["Destinations"] = aws_sdk_cloudtrail.types.destinations.serialize_aws_json_1_1(
        value["destinations"]
    )
    if "tags" in value:
        import aws_sdk_cloudtrail.types.tags_list

        out["Tags"] = aws_sdk_cloudtrail.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateChannelRequest:
    out: CreateChannelRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateChannelRequest.name required")
    if "Source" in data:
        out["source"] = data["Source"]
    else:
        raise DeserializationError("CreateChannelRequest.source required")
    if "Destinations" in data:
        import aws_sdk_cloudtrail.types.destinations

        out["destinations"] = (
            aws_sdk_cloudtrail.types.destinations.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    else:
        raise DeserializationError("CreateChannelRequest.destinations required")
    if "Tags" in data:
        import aws_sdk_cloudtrail.types.tags_list

        out["tags"] = aws_sdk_cloudtrail.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
