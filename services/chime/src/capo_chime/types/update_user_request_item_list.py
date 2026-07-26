"""Generated from Smithy shape ``com.amazonaws.chime#UpdateUserRequestItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.update_user_request_item

UpdateUserRequestItemList: TypeAlias = list[
    "capo_chime.types.update_user_request_item.UpdateUserRequestItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequestItemList) -> list:
    import capo_chime.types.update_user_request_item

    out: list = []
    for item in value:
        out.append(capo_chime.types.update_user_request_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateUserRequestItemList:
    import capo_chime.types.update_user_request_item

    out: UpdateUserRequestItemList = []
    for item in data:
        out.append(capo_chime.types.update_user_request_item.deserialize_json(item))
    return out
