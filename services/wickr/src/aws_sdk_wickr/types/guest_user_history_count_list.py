"""Generated from Smithy shape ``com.amazonaws.wickr#GuestUserHistoryCountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wickr.types.guest_user_history_count

GuestUserHistoryCountList: TypeAlias = list[
    "aws_sdk_wickr.types.guest_user_history_count.GuestUserHistoryCount"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuestUserHistoryCountList) -> list:
    import aws_sdk_wickr.types.guest_user_history_count

    out: list = []
    for item in value:
        out.append(aws_sdk_wickr.types.guest_user_history_count.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuestUserHistoryCountList:
    import aws_sdk_wickr.types.guest_user_history_count

    out: GuestUserHistoryCountList = []
    for item in data:
        out.append(aws_sdk_wickr.types.guest_user_history_count.deserialize_json(item))
    return out
