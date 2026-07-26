"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfInvitation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.invitation

__listOfInvitation: TypeAlias = list["capo_macie2.types.invitation.Invitation"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInvitation) -> list:
    import capo_macie2.types.invitation

    out: list = []
    for item in value:
        out.append(capo_macie2.types.invitation.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInvitation:
    import capo_macie2.types.invitation

    out: __listOfInvitation = []
    for item in data:
        out.append(capo_macie2.types.invitation.deserialize_json(item))
    return out
