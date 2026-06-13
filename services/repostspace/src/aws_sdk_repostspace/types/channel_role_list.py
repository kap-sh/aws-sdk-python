"""Generated from Smithy shape ``com.amazonaws.repostspace#ChannelRoleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.channel_role

ChannelRoleList: TypeAlias = list["aws_sdk_repostspace.types.channel_role.ChannelRole"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelRoleList) -> list:
    import aws_sdk_repostspace.types.channel_role

    out: list = []
    for item in value:
        out.append(aws_sdk_repostspace.types.channel_role.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChannelRoleList:
    import aws_sdk_repostspace.types.channel_role

    out: ChannelRoleList = []
    for item in data:
        out.append(aws_sdk_repostspace.types.channel_role.deserialize_json(item))
    return out
