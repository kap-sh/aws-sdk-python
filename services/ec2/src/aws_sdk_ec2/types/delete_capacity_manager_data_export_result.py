"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteCapacityManagerDataExportResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_data_export_id


class DeleteCapacityManagerDataExportResult(TypedDict):
    capacity_manager_data_export_id: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_data_export_id.CapacityManagerDataExportId"
    ]
    """<p> The unique identifier of the deleted data export configuration. </p>"""
