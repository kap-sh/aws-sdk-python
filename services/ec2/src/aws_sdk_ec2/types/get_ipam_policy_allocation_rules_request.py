"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPolicyAllocationRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.ipam_max_results
    import aws_sdk_ec2.types.ipam_policy_id
    import aws_sdk_ec2.types.ipam_policy_resource_type
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.string


class GetIpamPolicyAllocationRulesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_policy_id: NotRequired["aws_sdk_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy for which to get allocation rules.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters for the allocation rules.</p>"""
    locale: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The locale for which to get the allocation rules.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_resource_type.IpamPolicyResourceType"
    ]
    """<p>The resource type for which to get the allocation rules.</p> <p>The Amazon Web Services service or resource type that can use IP addresses through IPAM policies. Supported services and resource types include:</p> <ul> <li> <p>Elastic IP addresses</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.ipam_max_results.IpamMaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
