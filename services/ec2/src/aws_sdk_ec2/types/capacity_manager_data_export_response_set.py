"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerDataExportResponseSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_data_export_response

CapacityManagerDataExportResponseSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_manager_data_export_response.CapacityManagerDataExportResponse"
]
