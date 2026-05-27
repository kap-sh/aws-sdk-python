"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityManagerDataExportsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.capacity_manager_data_export_id_set
    import aws_sdk_ec2.types.describe_capacity_manager_data_exports_request_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeCapacityManagerDataExportsRequest(TypedDict):
    capacity_manager_data_export_ids: NotRequired[
        "aws_sdk_ec2.types.capacity_manager_data_export_id_set.CapacityManagerDataExportIdSet"
    ]
    """<p> The IDs of the data export configurations to describe. If not specified, all export configurations are returned. </p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_capacity_manager_data_exports_request_max_results.DescribeCapacityManagerDataExportsRequestMaxResults"
    ]
    """<p> The maximum number of results to return in a single call. If not specified, up to 1000 results are returned. </p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The token for the next page of results. Use this value in a subsequent call to retrieve additional results. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p> One or more filters to narrow the results. Supported filters include export status, creation date, and S3 bucket name. </p>"""
