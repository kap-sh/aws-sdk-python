"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareInvitationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.resource_share_invitation

ResourceShareInvitationList: TypeAlias = list[
    "capo_ram.types.resource_share_invitation.ResourceShareInvitation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareInvitationList) -> list:
    import capo_ram.types.resource_share_invitation

    out: list = []
    for item in value:
        out.append(capo_ram.types.resource_share_invitation.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceShareInvitationList:
    import capo_ram.types.resource_share_invitation

    out: ResourceShareInvitationList = []
    for item in data:
        out.append(capo_ram.types.resource_share_invitation.deserialize_json(item))
    return out
