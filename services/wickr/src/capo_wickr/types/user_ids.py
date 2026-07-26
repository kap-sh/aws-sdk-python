"""Generated from Smithy shape ``com.amazonaws.wickr#UserIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.user_id

UserIds: TypeAlias = list["capo_wickr.types.user_id.UserId"]


# --- restJson1 ser/de ---
def serialize_json(value: UserIds) -> list:
    return list(value)


def deserialize_json(data: list) -> UserIds:
    return list(data)
