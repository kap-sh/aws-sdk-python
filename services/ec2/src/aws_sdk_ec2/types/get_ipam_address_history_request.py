"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamAddressHistoryRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_address_history_max_results
    import aws_sdk_ec2.types.ipam_scope_id
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.string


class GetIpamAddressHistoryRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR you want the history of. The CIDR can be an IPv4 or IPv6 IP address range. If you enter a /16 IPv4 CIDR, you will get records that match it exactly. You will not get records for any subnets within the /16 CIDR.</p>"""
    ipam_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the IPAM scope that the CIDR is in.</p>"""
    vpc_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the VPC you want your history records filtered by.</p>"""
    start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start of the time period for which you are looking for history. If you omit this option, it will default to the value of EndTime.</p>"""
    end_time: NotRequired["aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The end of the time period for which you are looking for history. If you omit this option, it will default to the current time.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.ipam_address_history_max_results.IpamAddressHistoryMaxResults"
    ]
    """<p>The maximum number of historical results you would like returned per page. Defaults to 100.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
