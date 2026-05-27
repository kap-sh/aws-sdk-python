"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityManagerDataExportsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_data_export_response_set
    import aws_sdk_ec2.types.string


class DescribeCapacityManagerDataExportsResult(TypedDict):
    capacity_manager_data_exports: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_data_export_response_set.CapacityManagerDataExportResponseSet"
    ]
    """<p> Information about the data export configurations, including export settings, delivery status, and recent activity. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""
