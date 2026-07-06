"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CreateChannelGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.idempotency_token
    import aws_sdk_mediapackagev2.types.resource_description
    import aws_sdk_mediapackagev2.types.resource_name
    import aws_sdk_mediapackagev2.types.tag_map


class CreateChannelGroupRequest(TypedDict, closed=True):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region. You can't use spaces in the name. You can't change the name after you create the channel group.</p>"""
    client_token: NotRequired[
        "aws_sdk_mediapackagev2.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>"""
    description: NotRequired[
        "aws_sdk_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>Enter any descriptive text that helps you to identify the channel group.</p>"""
    tags: NotRequired["aws_sdk_mediapackagev2.types.tag_map.TagMap"]
    r"""<p>A comma-separated list of tag key:value pairs that you define. For example:</p> <p> <code>\"Key1\": \"Value1\",</code> </p> <p> <code>\"Key2\": \"Value2\"</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelGroupRequest) -> dict:
    out: dict = {}
    out["ChannelGroupName"] = value["channel_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_mediapackagev2.types.tag_map

        out["tags"] = aws_sdk_mediapackagev2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateChannelGroupRequest:
    out: CreateChannelGroupRequest = {}  # type: ignore[typeddict-item]
    if "ChannelGroupName" in data:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError(
            "CreateChannelGroupRequest.channel_group_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "tags" in data:
        import aws_sdk_mediapackagev2.types.tag_map

        out["tags"] = aws_sdk_mediapackagev2.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
