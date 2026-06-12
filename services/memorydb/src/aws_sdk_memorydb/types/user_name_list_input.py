"""Generated from Smithy shape ``com.amazonaws.memorydb#UserNameListInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.user_name

UserNameListInput: TypeAlias = list["aws_sdk_memorydb.types.user_name.UserName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserNameListInput) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> UserNameListInput:
    return list(data)
