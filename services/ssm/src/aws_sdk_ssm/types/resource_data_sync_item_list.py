"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_data_sync_item

ResourceDataSyncItemList: TypeAlias = list[
    "aws_sdk_ssm.types.resource_data_sync_item.ResourceDataSyncItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncItemList) -> list:
    import aws_sdk_ssm.types.resource_data_sync_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm.types.resource_data_sync_item.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceDataSyncItemList:
    import aws_sdk_ssm.types.resource_data_sync_item

    out: ResourceDataSyncItemList = []
    for item in data:
        out.append(
            aws_sdk_ssm.types.resource_data_sync_item.deserialize_aws_json_1_1(item)
        )
    return out
