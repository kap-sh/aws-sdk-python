"""Generated from Smithy shape ``com.amazonaws.wickr#GuestUserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.guest_user

GuestUserList: TypeAlias = list["capo_wickr.types.guest_user.GuestUser"]


# --- restJson1 ser/de ---
def serialize_json(value: GuestUserList) -> list:
    import capo_wickr.types.guest_user

    out: list = []
    for item in value:
        out.append(capo_wickr.types.guest_user.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuestUserList:
    import capo_wickr.types.guest_user

    out: GuestUserList = []
    for item in data:
        out.append(capo_wickr.types.guest_user.deserialize_json(item))
    return out
