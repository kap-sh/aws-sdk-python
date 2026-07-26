"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ChannelGroupListConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mediapackagev2.types.resource_description


class ChannelGroupListConfiguration(TypedDict, closed=True):
    channel_group_name: "str"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the resource.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the channel group was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the channel group was modified.</p>"""
    description: NotRequired[
        "capo_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>Any descriptive information that you want to add to the channel group for future identification purposes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelGroupListConfiguration) -> dict:
    out: dict = {}
    out["ChannelGroupName"] = value["channel_group_name"]
    out["Arn"] = value["arn"]
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
    return out


def deserialize_json(data: dict) -> ChannelGroupListConfiguration:
    out: ChannelGroupListConfiguration = {}  # type: ignore[typeddict-item]
    if "ChannelGroupName" in data:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError(
            "ChannelGroupListConfiguration.channel_group_name required"
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ChannelGroupListConfiguration.arn required")
    if "CreatedAt" in data:
        import capo_mediapackagev2.types._prelude.timestamp

        out["created_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("ChannelGroupListConfiguration.created_at required")
    if "ModifiedAt" in data:
        import capo_mediapackagev2.types._prelude.timestamp

        out["modified_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ModifiedAt"]
            )
        )
    else:
        raise DeserializationError("ChannelGroupListConfiguration.modified_at required")
    if "Description" in data:
        out["description"] = data["Description"]
    return out
