"""Generated from Smithy shape ``com.amazonaws.repostspace#ChannelData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_repostspace.types.channel_description
    import aws_sdk_repostspace.types.channel_id
    import aws_sdk_repostspace.types.channel_name
    import aws_sdk_repostspace.types.channel_status
    import aws_sdk_repostspace.types.group_count
    import aws_sdk_repostspace.types.space_id
    import aws_sdk_repostspace.types.user_count


class ChannelData(TypedDict, closed=True):
    space_id: "aws_sdk_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    channel_id: "aws_sdk_repostspace.types.channel_id.ChannelId"
    """<p>The unique ID of the private re:Post channel.</p>"""
    channel_name: "aws_sdk_repostspace.types.channel_name.ChannelName"
    """<p>The name for the channel. This must be unique per private re:Post.</p>"""
    channel_description: NotRequired[
        "aws_sdk_repostspace.types.channel_description.ChannelDescription"
    ]
    """<p>A description for the channel. This is used only to help you identify this channel.</p>"""
    create_date_time: "datetime.datetime"
    """<p>The date when the channel was created.</p>"""
    delete_date_time: NotRequired["datetime.datetime"]
    """<p>The date when the channel was deleted.</p>"""
    channel_status: "aws_sdk_repostspace.types.channel_status.ChannelStatus"
    """<p>The status pf the channel.</p>"""
    user_count: "aws_sdk_repostspace.types.user_count.UserCount"
    """<p>The number of users that are part of the channel.</p>"""
    group_count: "aws_sdk_repostspace.types.group_count.GroupCount"
    """<p>The number of groups that are part of the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelData) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["channelId"] = value["channel_id"]
    out["channelName"] = value["channel_name"]
    if "channel_description" in value:
        out["channelDescription"] = value["channel_description"]
    import aws_sdk_repostspace.types._prelude.timestamp

    out["createDateTime"] = aws_sdk_repostspace.types._prelude.timestamp.serialize_json(
        value["create_date_time"]
    )
    if "delete_date_time" in value:
        import aws_sdk_repostspace.types._prelude.timestamp

        out["deleteDateTime"] = (
            aws_sdk_repostspace.types._prelude.timestamp.serialize_json(
                value["delete_date_time"]
            )
        )
    import aws_sdk_repostspace.types.channel_status

    out["channelStatus"] = aws_sdk_repostspace.types.channel_status.serialize_json(
        value["channel_status"]
    )
    out["userCount"] = value["user_count"]
    out["groupCount"] = value["group_count"]
    return out


def deserialize_json(data: dict) -> ChannelData:
    out: ChannelData = {}  # type: ignore[typeddict-item]
    if "spaceId" in data:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("ChannelData.space_id required")
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    else:
        raise DeserializationError("ChannelData.channel_id required")
    if "channelName" in data:
        out["channel_name"] = data["channelName"]
    else:
        raise DeserializationError("ChannelData.channel_name required")
    if "channelDescription" in data:
        out["channel_description"] = data["channelDescription"]
    if "createDateTime" in data:
        import aws_sdk_repostspace.types._prelude.timestamp

        out["create_date_time"] = (
            aws_sdk_repostspace.types._prelude.timestamp.deserialize_json(
                data["createDateTime"]
            )
        )
    else:
        raise DeserializationError("ChannelData.create_date_time required")
    if "deleteDateTime" in data:
        import aws_sdk_repostspace.types._prelude.timestamp

        out["delete_date_time"] = (
            aws_sdk_repostspace.types._prelude.timestamp.deserialize_json(
                data["deleteDateTime"]
            )
        )
    if "channelStatus" in data:
        import aws_sdk_repostspace.types.channel_status

        out["channel_status"] = (
            aws_sdk_repostspace.types.channel_status.deserialize_json(
                data["channelStatus"]
            )
        )
    else:
        raise DeserializationError("ChannelData.channel_status required")
    if "userCount" in data:
        out["user_count"] = data["userCount"]
    else:
        raise DeserializationError("ChannelData.user_count required")
    if "groupCount" in data:
        out["group_count"] = data["groupCount"]
    else:
        raise DeserializationError("ChannelData.group_count required")
    return out
