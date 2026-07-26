"""Generated from Smithy shape ``com.amazonaws.connect#UserIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.user_id

UserIdList: TypeAlias = list["capo_connect.types.user_id.UserId"]


# --- restJson1 ser/de ---
def serialize_json(value: UserIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> UserIdList:
    return list(data)
