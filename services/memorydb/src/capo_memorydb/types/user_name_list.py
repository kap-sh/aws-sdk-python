"""Generated from Smithy shape ``com.amazonaws.memorydb#UserNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.user_name

UserNameList: TypeAlias = list["capo_memorydb.types.user_name.UserName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> UserNameList:
    return list(data)
