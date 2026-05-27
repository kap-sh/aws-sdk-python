"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityManagerDataExportResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_data_export_id


class CreateCapacityManagerDataExportResult(TypedDict):
    capacity_manager_data_export_id: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_data_export_id.CapacityManagerDataExportId"
    ]
    """<p> The unique identifier for the created data export configuration. Use this ID to reference the export in other API calls. </p>"""
