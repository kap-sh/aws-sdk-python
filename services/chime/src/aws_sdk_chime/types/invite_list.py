"""Generated from Smithy shape ``com.amazonaws.chime#InviteList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime.types.invite

InviteList: TypeAlias = list["aws_sdk_chime.types.invite.Invite"]


# --- restJson1 ser/de ---
def serialize_json(value: InviteList) -> list:
    import aws_sdk_chime.types.invite

    out: list = []
    for item in value:
        out.append(aws_sdk_chime.types.invite.serialize_json(item))
    return out


def deserialize_json(data: list) -> InviteList:
    import aws_sdk_chime.types.invite

    out: InviteList = []
    for item in data:
        out.append(aws_sdk_chime.types.invite.deserialize_json(item))
    return out
