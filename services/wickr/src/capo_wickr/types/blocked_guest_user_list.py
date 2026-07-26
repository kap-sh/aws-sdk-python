"""Generated from Smithy shape ``com.amazonaws.wickr#BlockedGuestUserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.blocked_guest_user

BlockedGuestUserList: TypeAlias = list[
    "capo_wickr.types.blocked_guest_user.BlockedGuestUser"
]


# --- restJson1 ser/de ---
def serialize_json(value: BlockedGuestUserList) -> list:
    import capo_wickr.types.blocked_guest_user

    out: list = []
    for item in value:
        out.append(capo_wickr.types.blocked_guest_user.serialize_json(item))
    return out


def deserialize_json(data: list) -> BlockedGuestUserList:
    import capo_wickr.types.blocked_guest_user

    out: BlockedGuestUserList = []
    for item in data:
        out.append(capo_wickr.types.blocked_guest_user.deserialize_json(item))
    return out
