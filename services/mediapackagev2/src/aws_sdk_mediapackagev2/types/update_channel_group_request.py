"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#UpdateChannelGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.entity_tag
    import aws_sdk_mediapackagev2.types.resource_description
    import aws_sdk_mediapackagev2.types.resource_name


class UpdateChannelGroupRequest(TypedDict):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    e_tag: NotRequired["aws_sdk_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The expected current Entity Tag (ETag) for the resource. If the specified ETag does not match the resource's current entity tag, the update request will be rejected.</p>"""
    description: NotRequired[
        "aws_sdk_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>Any descriptive information that you want to add to the channel group for future identification purposes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateChannelGroupRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateChannelGroupRequest:
    out: UpdateChannelGroupRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
