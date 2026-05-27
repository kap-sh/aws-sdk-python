"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroupVpcAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_security_group_vpc_associations_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeSecurityGroupVpcAssociationsRequest(TypedDict):
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>Security group VPC association filters.</p> <ul> <li> <p> <code>group-id</code>: The security group ID.</p> </li> <li> <p> <code>group-owner-id</code>: The group owner ID.</p> </li> <li> <p> <code>state</code>: The state of the association.</p> </li> <li> <p> <code>vpc-id</code>: The ID of the associated VPC.</p> </li> <li> <p> <code>vpc-owner-id</code>: The account ID of the VPC owner.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_security_group_vpc_associations_max_results.DescribeSecurityGroupVpcAssociationsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
