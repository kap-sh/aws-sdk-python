"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_vpcs_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_id_string_list


class DescribeVpcsRequest(TypedDict):
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>cidr</code> - The primary IPv4 CIDR block of the VPC. The CIDR block you specify must exactly match the VPC's CIDR block for information to be returned for the VPC. Must contain the slash followed by one or two digits (for example, <code>/28</code>).</p> </li> <li> <p> <code>cidr-block-association.cidr-block</code> - An IPv4 CIDR block associated with the VPC.</p> </li> <li> <p> <code>cidr-block-association.association-id</code> - The association ID for an IPv4 CIDR block associated with the VPC.</p> </li> <li> <p> <code>cidr-block-association.state</code> - The state of an IPv4 CIDR block associated with the VPC.</p> </li> <li> <p> <code>dhcp-options-id</code> - The ID of a set of DHCP options.</p> </li> <li> <p> <code>ipv6-cidr-block-association.ipv6-cidr-block</code> - An IPv6 CIDR block associated with the VPC.</p> </li> <li> <p> <code>ipv6-cidr-block-association.ipv6-pool</code> - The ID of the IPv6 address pool from which the IPv6 CIDR block is allocated.</p> </li> <li> <p> <code>ipv6-cidr-block-association.association-id</code> - The association ID for an IPv6 CIDR block associated with the VPC.</p> </li> <li> <p> <code>ipv6-cidr-block-association.state</code> - The state of an IPv6 CIDR block associated with the VPC.</p> </li> <li> <p> <code>is-default</code> - Indicates whether the VPC is the default VPC.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the VPC.</p> </li> <li> <p> <code>state</code> - The state of the VPC (<code>pending</code> | <code>available</code>).</p> </li> <li> <p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>vpc-id</code> - The ID of the VPC.</p> </li> </ul>"""
    vpc_ids: NotRequired["aws_sdk_ec2.types.vpc_id_string_list.VpcIdStringList"]
    """<p>The IDs of the VPCs.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_vpcs_max_results.DescribeVpcsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
