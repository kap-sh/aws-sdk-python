"""Generated from Smithy shape ``com.amazonaws.connect#UserDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.user_data

UserDataList: TypeAlias = list["aws_sdk_connect.types.user_data.UserData"]


# --- restJson1 ser/de ---
def serialize_json(value: UserDataList) -> list:
    import aws_sdk_connect.types.user_data

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.user_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserDataList:
    import aws_sdk_connect.types.user_data

    out: UserDataList = []
    for item in data:
        out.append(aws_sdk_connect.types.user_data.deserialize_json(item))
    return out
