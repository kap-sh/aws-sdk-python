"""Generated from Smithy shape ``com.amazonaws.wickr#GuestUserHistoryCountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.guest_user_history_count

GuestUserHistoryCountList: TypeAlias = list[
    "capo_wickr.types.guest_user_history_count.GuestUserHistoryCount"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuestUserHistoryCountList) -> list:
    import capo_wickr.types.guest_user_history_count

    out: list = []
    for item in value:
        out.append(capo_wickr.types.guest_user_history_count.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuestUserHistoryCountList:
    import capo_wickr.types.guest_user_history_count

    out: GuestUserHistoryCountList = []
    for item in data:
        out.append(capo_wickr.types.guest_user_history_count.deserialize_json(item))
    return out
