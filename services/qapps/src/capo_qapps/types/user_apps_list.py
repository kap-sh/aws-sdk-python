"""Generated from Smithy shape ``com.amazonaws.qapps#UserAppsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.user_app_item

UserAppsList: TypeAlias = list["capo_qapps.types.user_app_item.UserAppItem"]


# --- restJson1 ser/de ---
def serialize_json(value: UserAppsList) -> list:
    import capo_qapps.types.user_app_item

    out: list = []
    for item in value:
        out.append(capo_qapps.types.user_app_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserAppsList:
    import capo_qapps.types.user_app_item

    out: UserAppsList = []
    for item in data:
        out.append(capo_qapps.types.user_app_item.deserialize_json(item))
    return out
