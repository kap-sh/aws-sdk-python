"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEncryptionControlsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_vpc_encryption_controls_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_encryption_control_id_list
    import aws_sdk_ec2.types.vpc_id_string_list


class DescribeVpcEncryptionControlsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters to apply to the request.</p>"""
    vpc_encryption_control_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_id_list.VpcEncryptionControlIdList"
    ]
    """<p>The IDs of the VPC Encryption Control configurations to describe.</p>"""
    vpc_ids: NotRequired["aws_sdk_ec2.types.vpc_id_string_list.VpcIdStringList"]
    """<p>The IDs of the VPCs to describe encryption control configurations for.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_vpc_encryption_controls_max_results.DescribeVpcEncryptionControlsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
