"""Generated from Smithy shape ``com.amazonaws.ec2#GetSecurityGroupsForVpcRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.get_security_groups_for_vpc_request_max_results
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_id


class GetSecurityGroupsForVpcRequest(TypedDict):
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The VPC ID where the security group can be used.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.get_security_groups_for_vpc_request_max_results.GetSecurityGroupsForVpcRequestMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters. If using multiple filters, the results include security groups which match all filters.</p> <ul> <li> <p> <code>group-id</code>: The security group ID.</p> </li> <li> <p> <code>description</code>: The security group's description.</p> </li> <li> <p> <code>group-name</code>: The security group name.</p> </li> <li> <p> <code>owner-id</code>: The security group owner ID.</p> </li> <li> <p> <code>primary-vpc-id</code>: The VPC ID in which the security group was created.</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
