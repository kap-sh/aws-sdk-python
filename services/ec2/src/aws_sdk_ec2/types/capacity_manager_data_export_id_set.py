"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerDataExportIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_data_export_id

CapacityManagerDataExportIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_manager_data_export_id.CapacityManagerDataExportId"
]
