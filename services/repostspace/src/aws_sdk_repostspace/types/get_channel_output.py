"""Generated from Smithy shape ``com.amazonaws.repostspace#GetChannelOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_repostspace.types.channel_description
    import aws_sdk_repostspace.types.channel_id
    import aws_sdk_repostspace.types.channel_name
    import aws_sdk_repostspace.types.channel_roles
    import aws_sdk_repostspace.types.channel_status
    import aws_sdk_repostspace.types.space_id


class GetChannelOutput(TypedDict, closed=True):
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
    channel_roles: NotRequired["aws_sdk_repostspace.types.channel_roles.ChannelRoles"]
    """<p>The channel roles associated to the users and groups of the channel.</p>"""
    channel_status: "aws_sdk_repostspace.types.channel_status.ChannelStatus"
    """<p>The status pf the channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChannelOutput) -> dict:
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
    if "channel_roles" in value:
        import aws_sdk_repostspace.types.channel_roles

        out["channelRoles"] = aws_sdk_repostspace.types.channel_roles.serialize_json(
            value["channel_roles"]
        )
    import aws_sdk_repostspace.types.channel_status

    out["channelStatus"] = aws_sdk_repostspace.types.channel_status.serialize_json(
        value["channel_status"]
    )
    return out


def deserialize_json(data: dict) -> GetChannelOutput:
    out: GetChannelOutput = {}  # type: ignore[typeddict-item]
    if "spaceId" in data:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("GetChannelOutput.space_id required")
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    else:
        raise DeserializationError("GetChannelOutput.channel_id required")
    if "channelName" in data:
        out["channel_name"] = data["channelName"]
    else:
        raise DeserializationError("GetChannelOutput.channel_name required")
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
        raise DeserializationError("GetChannelOutput.create_date_time required")
    if "deleteDateTime" in data:
        import aws_sdk_repostspace.types._prelude.timestamp

        out["delete_date_time"] = (
            aws_sdk_repostspace.types._prelude.timestamp.deserialize_json(
                data["deleteDateTime"]
            )
        )
    if "channelRoles" in data:
        import aws_sdk_repostspace.types.channel_roles

        out["channel_roles"] = aws_sdk_repostspace.types.channel_roles.deserialize_json(
            data["channelRoles"]
        )
    if "channelStatus" in data:
        import aws_sdk_repostspace.types.channel_status

        out["channel_status"] = (
            aws_sdk_repostspace.types.channel_status.deserialize_json(
                data["channelStatus"]
            )
        )
    else:
        raise DeserializationError("GetChannelOutput.channel_status required")
    return out
