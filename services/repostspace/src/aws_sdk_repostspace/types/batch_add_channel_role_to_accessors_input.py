"""Generated from Smithy shape ``com.amazonaws.repostspace#BatchAddChannelRoleToAccessorsInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_repostspace.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_repostspace.types.accessor_id_list
    import aws_sdk_repostspace.types.channel_id
    import aws_sdk_repostspace.types.channel_role
    import aws_sdk_repostspace.types.space_id

class BatchAddChannelRoleToAccessorsInput(TypedDict):
    space_id: "aws_sdk_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""
    channel_id: "aws_sdk_repostspace.types.channel_id.ChannelId"
    """<p>The unique ID of the private re:Post channel.</p>"""
    accessor_ids: "aws_sdk_repostspace.types.accessor_id_list.AccessorIdList"
    """<p>The user or group identifiers to add the role to.</p>"""
    channel_role: "aws_sdk_repostspace.types.channel_role.ChannelRole"
    """<p>The channel role to add to the users or groups.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchAddChannelRoleToAccessorsInput) -> dict:
    out: dict = {}
    import aws_sdk_repostspace.types.accessor_id_list
    out["accessorIds"] = aws_sdk_repostspace.types.accessor_id_list.serialize_json(value["accessor_ids"])
    import aws_sdk_repostspace.types.channel_role
    out["channelRole"] = aws_sdk_repostspace.types.channel_role.serialize_json(value["channel_role"])
    return out


def deserialize_json(data: dict) -> BatchAddChannelRoleToAccessorsInput:
    out: BatchAddChannelRoleToAccessorsInput = {}  # type: ignore[typeddict-item]
    if "accessorIds" in data:
        import aws_sdk_repostspace.types.accessor_id_list
        out["accessor_ids"] = aws_sdk_repostspace.types.accessor_id_list.deserialize_json(data["accessorIds"])
    else:
        raise DeserializationError("BatchAddChannelRoleToAccessorsInput.accessor_ids required")
    if "channelRole" in data:
        import aws_sdk_repostspace.types.channel_role
        out["channel_role"] = aws_sdk_repostspace.types.channel_role.deserialize_json(data["channelRole"])
    else:
        raise DeserializationError("BatchAddChannelRoleToAccessorsInput.channel_role required")
    return out