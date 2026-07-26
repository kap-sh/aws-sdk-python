"""Generated from Smithy shape ``com.amazonaws.repostspace#ChannelRoles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_repostspace.types.accessor_id
    import capo_repostspace.types.channel_role_list

ChannelRoles: TypeAlias = dict[
    "capo_repostspace.types.accessor_id.AccessorId",
    "capo_repostspace.types.channel_role_list.ChannelRoleList",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ChannelRoles) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_repostspace.types.channel_role_list

        out[key] = capo_repostspace.types.channel_role_list.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ChannelRoles:
    out: ChannelRoles = {}
    for key, value in data.items():
        import capo_repostspace.types.channel_role_list

        out[key] = capo_repostspace.types.channel_role_list.deserialize_json(value)
    return out
