"""Generated from Smithy shape ``com.amazonaws.fms#FailedItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.failed_item

FailedItemList: TypeAlias = list["aws_sdk_fms.types.failed_item.FailedItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedItemList) -> list:
    import aws_sdk_fms.types.failed_item

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.failed_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FailedItemList:
    import aws_sdk_fms.types.failed_item

    out: FailedItemList = []
    for item in data:
        out.append(aws_sdk_fms.types.failed_item.deserialize_aws_json_1_1(item))
    return out
