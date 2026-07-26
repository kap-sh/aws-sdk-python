"""Generated from Smithy shape ``com.amazonaws.storagegateway#UserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.user_list_user

UserList: TypeAlias = list["capo_storage_gateway.types.user_list_user.UserListUser"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> UserList:
    return list(data)
