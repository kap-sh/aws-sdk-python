"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetChannelGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mediapackagev2.types.entity_tag
    import aws_sdk_mediapackagev2.types.resource_description
    import aws_sdk_mediapackagev2.types.tag_map


class GetChannelGroupResponse(TypedDict):
    channel_group_name: "str"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the resource.</p>"""
    egress_domain: "str"
    """<p>The output domain where the source stream should be sent. Integrate the domain with a downstream CDN (such as Amazon CloudFront) or playback device.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the channel group was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the channel group was modified.</p>"""
    description: NotRequired[
        "aws_sdk_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>The description for your channel group.</p>"""
    e_tag: NotRequired["aws_sdk_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.</p>"""
    tags: NotRequired["aws_sdk_mediapackagev2.types.tag_map.TagMap"]
    """<p>The comma-separated list of tag key:value pairs assigned to the channel group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelGroupResponse) -> dict:
    out: dict = {}
    out["ChannelGroupName"] = value["channel_group_name"]
    out["Arn"] = value["arn"]
    out["EgressDomain"] = value["egress_domain"]
    import aws_sdk_mediapackagev2.types._prelude.timestamp

    out["CreatedAt"] = aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_mediapackagev2.types._prelude.timestamp

    out["ModifiedAt"] = aws_sdk_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "tags" in value:
        import aws_sdk_mediapackagev2.types.tag_map

        out["tags"] = aws_sdk_mediapackagev2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetChannelGroupResponse:
    out: GetChannelGroupResponse = {}  # type: ignore[typeddict-item]
    if "ChannelGroupName" in data:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError(
            "GetChannelGroupResponse.channel_group_name required"
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetChannelGroupResponse.arn required")
    if "EgressDomain" in data:
        out["egress_domain"] = data["EgressDomain"]
    else:
        raise DeserializationError("GetChannelGroupResponse.egress_domain required")
    if "CreatedAt" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("GetChannelGroupResponse.created_at required")
    if "ModifiedAt" in data:
        import aws_sdk_mediapackagev2.types._prelude.timestamp

        out["modified_at"] = (
            aws_sdk_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ModifiedAt"]
            )
        )
    else:
        raise DeserializationError("GetChannelGroupResponse.modified_at required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    if "tags" in data:
        import aws_sdk_mediapackagev2.types.tag_map

        out["tags"] = aws_sdk_mediapackagev2.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
