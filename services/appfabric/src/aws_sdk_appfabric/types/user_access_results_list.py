"""Generated from Smithy shape ``com.amazonaws.appfabric#UserAccessResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appfabric.types.user_access_result_item

UserAccessResultsList: TypeAlias = list[
    "aws_sdk_appfabric.types.user_access_result_item.UserAccessResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserAccessResultsList) -> list:
    import aws_sdk_appfabric.types.user_access_result_item

    out: list = []
    for item in value:
        out.append(aws_sdk_appfabric.types.user_access_result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserAccessResultsList:
    import aws_sdk_appfabric.types.user_access_result_item

    out: UserAccessResultsList = []
    for item in data:
        out.append(
            aws_sdk_appfabric.types.user_access_result_item.deserialize_json(item)
        )
    return out
