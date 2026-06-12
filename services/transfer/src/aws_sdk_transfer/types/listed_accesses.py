"""Generated from Smithy shape ``com.amazonaws.transfer#ListedAccesses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_access

ListedAccesses: TypeAlias = list["aws_sdk_transfer.types.listed_access.ListedAccess"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedAccesses) -> list:
    import aws_sdk_transfer.types.listed_access

    out: list = []
    for item in value:
        out.append(aws_sdk_transfer.types.listed_access.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListedAccesses:
    import aws_sdk_transfer.types.listed_access

    out: ListedAccesses = []
    for item in data:
        out.append(aws_sdk_transfer.types.listed_access.deserialize_aws_json_1_1(item))
    return out
