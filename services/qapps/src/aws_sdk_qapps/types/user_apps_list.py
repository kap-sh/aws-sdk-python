"""Generated from Smithy shape ``com.amazonaws.qapps#UserAppsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qapps.types.user_app_item

UserAppsList: TypeAlias = list["aws_sdk_qapps.types.user_app_item.UserAppItem"]


# --- restJson1 ser/de ---
def serialize_json(value: UserAppsList) -> list:
    import aws_sdk_qapps.types.user_app_item

    out: list = []
    for item in value:
        out.append(aws_sdk_qapps.types.user_app_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserAppsList:
    import aws_sdk_qapps.types.user_app_item

    out: UserAppsList = []
    for item in data:
        out.append(aws_sdk_qapps.types.user_app_item.deserialize_json(item))
    return out
