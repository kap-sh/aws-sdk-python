"""Generated from Smithy shape ``com.amazonaws.guardduty#Invitations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.invitation

Invitations: TypeAlias = list["capo_guardduty.types.invitation.Invitation"]


# --- restJson1 ser/de ---
def serialize_json(value: Invitations) -> list:
    import capo_guardduty.types.invitation

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.invitation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Invitations:
    import capo_guardduty.types.invitation

    out: Invitations = []
    for item in data:
        out.append(capo_guardduty.types.invitation.deserialize_json(item))
    return out
