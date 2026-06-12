"""Generated from Smithy shape ``com.amazonaws.transfer#ListedUsers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_user

ListedUsers: TypeAlias = list["aws_sdk_transfer.types.listed_user.ListedUser"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedUsers) -> list:
    import aws_sdk_transfer.types.listed_user

    out: list = []
    for item in value:
        out.append(aws_sdk_transfer.types.listed_user.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListedUsers:
    import aws_sdk_transfer.types.listed_user

    out: ListedUsers = []
    for item in data:
        out.append(aws_sdk_transfer.types.listed_user.deserialize_aws_json_1_1(item))
    return out
