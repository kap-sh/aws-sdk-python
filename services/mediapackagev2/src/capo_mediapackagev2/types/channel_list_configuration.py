"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ChannelListConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mediapackagev2.types.input_type
    import capo_mediapackagev2.types.resource_description


class ChannelListConfiguration(TypedDict, closed=True):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the resource.</p>"""
    channel_name: "str"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>"""
    channel_group_name: "str"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the channel was created.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the channel was modified.</p>"""
    description: NotRequired[
        "capo_mediapackagev2.types.resource_description.ResourceDescription"
    ]
    """<p>Any descriptive information that you want to add to the channel for future identification purposes.</p>"""
    input_type: NotRequired["capo_mediapackagev2.types.input_type.InputType"]
    """<p>The input type will be an immutable field which will be used to define whether the channel will allow CMAF ingest or HLS ingest. If unprovided, it will default to HLS to preserve current behavior.</p> <p>The allowed values are:</p> <ul> <li> <p> <code>HLS</code> - The HLS streaming specification (which defines M3U8 manifests and TS segments).</p> </li> <li> <p> <code>CMAF</code> - The DASH-IF CMAF Ingest specification (which defines CMAF segments with optional DASH manifests).</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelListConfiguration) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["ChannelName"] = value["channel_name"]
    out["ChannelGroupName"] = value["channel_group_name"]
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
    if "input_type" in value:
        import capo_mediapackagev2.types.input_type

        out["InputType"] = capo_mediapackagev2.types.input_type.serialize_json(
            value["input_type"]
        )
    return out


def deserialize_json(data: dict) -> ChannelListConfiguration:
    out: ChannelListConfiguration = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ChannelListConfiguration.arn required")
    if "ChannelName" in data:
        out["channel_name"] = data["ChannelName"]
    else:
        raise DeserializationError("ChannelListConfiguration.channel_name required")
    if "ChannelGroupName" in data:
        out["channel_group_name"] = data["ChannelGroupName"]
    else:
        raise DeserializationError(
            "ChannelListConfiguration.channel_group_name required"
        )
    if "CreatedAt" in data:
        import capo_mediapackagev2.types._prelude.timestamp

        out["created_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("ChannelListConfiguration.created_at required")
    if "ModifiedAt" in data:
        import capo_mediapackagev2.types._prelude.timestamp

        out["modified_at"] = (
            capo_mediapackagev2.types._prelude.timestamp.deserialize_json(
                data["ModifiedAt"]
            )
        )
    else:
        raise DeserializationError("ChannelListConfiguration.modified_at required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "InputType" in data:
        import capo_mediapackagev2.types.input_type

        out["input_type"] = capo_mediapackagev2.types.input_type.deserialize_json(
            data["InputType"]
        )
    return out
