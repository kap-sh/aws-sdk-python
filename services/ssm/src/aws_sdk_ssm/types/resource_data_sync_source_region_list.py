"""Generated from Smithy shape ``com.amazonaws.ssm#ResourceDataSyncSourceRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.resource_data_sync_source_region

ResourceDataSyncSourceRegionList: TypeAlias = list[
    "aws_sdk_ssm.types.resource_data_sync_source_region.ResourceDataSyncSourceRegion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDataSyncSourceRegionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ResourceDataSyncSourceRegionList:
    return list(data)
