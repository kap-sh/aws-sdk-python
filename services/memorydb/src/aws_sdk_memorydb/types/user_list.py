"""Generated from Smithy shape ``com.amazonaws.memorydb#UserList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.user

UserList: TypeAlias = list["aws_sdk_memorydb.types.user.User"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserList) -> list:
    import aws_sdk_memorydb.types.user

    out: list = []
    for item in value:
        out.append(aws_sdk_memorydb.types.user.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> UserList:
    import aws_sdk_memorydb.types.user

    out: UserList = []
    for item in data:
        out.append(aws_sdk_memorydb.types.user.deserialize_aws_json_1_1(item))
    return out
