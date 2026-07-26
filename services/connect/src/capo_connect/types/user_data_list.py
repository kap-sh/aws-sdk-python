"""Generated from Smithy shape ``com.amazonaws.connect#UserDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.user_data

UserDataList: TypeAlias = list["capo_connect.types.user_data.UserData"]


# --- restJson1 ser/de ---
def serialize_json(value: UserDataList) -> list:
    import capo_connect.types.user_data

    out: list = []
    for item in value:
        out.append(capo_connect.types.user_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserDataList:
    import capo_connect.types.user_data

    out: UserDataList = []
    for item in data:
        out.append(capo_connect.types.user_data.deserialize_json(item))
    return out
