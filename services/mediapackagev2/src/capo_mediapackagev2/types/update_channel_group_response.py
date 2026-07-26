"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#UpdateChannelGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mediapackagev2.types.entity_tag
    import capo_mediapackagev2.types.resource_description
    import capo_mediapackagev2.types.tag_map


class UpdateChannelGroupResponse(TypedDict, closed=True):
    channel_group_name: "str"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the resource.</p>"""
    egress_domain: "str"
    """<p>The output domain where the source stream is sent. Integrate the domain with a downstream CDN (such as Amazon CloudFront) or playback device.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the channel group was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the channel group was modified.</p>"""
    description: NotRequired[
        "capo_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>The description for your channel group.</p>"""
    e_tag: NotRequired["capo_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The current Entity Tag (ETag) associated with this resource. The entity tag can be used to safely make concurrent updates to the resource.</p>"""
    tags: NotRequired["capo_mediapackagev2.types.tag_map.TagMap"]
    """<p>The comma-separated list of tag key:value pairs assigned to the channel group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelGroupResponse) -> dict:
    out: dict = {}
    out["ChannelGroupName"] = value["channel_group_name"]
    out["Arn"] = value["arn"]
    out["EgressDomain"] = value["egress_domain"]
    import capo_mediapackagev2.types._prelude.timestamp

    out["CreatedAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_mediapackagev2.types._prelude.timestamp

    out["ModifiedAt"] = capo_mediapackagev2.types._prelude.timestamp.serialize_json(
        value["modified_at"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "tags" in value:
        import capo_mediapackagev2.types.tag_map

        out["tags"] = capo_mediapackagev2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateChannelGroupResponse:
    out: UpdateChannelGroupResponse = {}  # type: ignore[typeddict-item]
    if "ChannelGroupName" in data:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError(
            "UpdateChannelGroupResponse.channel_group_name required"
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateChannelGroupResponse.arn required")
    if "EgressDomain" in data:
        out["egress_domain"] = data["EgressDomain"]
    else:
        raise DeserializationError("UpdateChannelGroupResponse.egress_domain required")
    if "CreatedAt" in data:
        import capo_mediapackagev2.types._prelude.timestamp

        out["created_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateChannelGroupResponse.created_at required")
    if "ModifiedAt" in data:
        import capo_mediapackagev2.types._prelude.timestamp

        out["modified_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ModifiedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateChannelGroupResponse.modified_at required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    if "tags" in data:
        import capo_mediapackagev2.types.tag_map

        out["tags"] = capo_mediapackagev2.types.tag_map.deserialize_json(data["tags"])
    return out
