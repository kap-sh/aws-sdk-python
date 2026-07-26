"""Generated from Smithy shape ``com.amazonaws.repostspace#ChannelRoleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_repostspace.types.channel_role

ChannelRoleList: TypeAlias = list["capo_repostspace.types.channel_role.ChannelRole"]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelRoleList) -> list:
    import capo_repostspace.types.channel_role

    out: list = []
    for item in value:
        out.append(capo_repostspace.types.channel_role.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChannelRoleList:
    import capo_repostspace.types.channel_role

    out: ChannelRoleList = []
    for item in data:
        out.append(capo_repostspace.types.channel_role.deserialize_json(item))
    return out
