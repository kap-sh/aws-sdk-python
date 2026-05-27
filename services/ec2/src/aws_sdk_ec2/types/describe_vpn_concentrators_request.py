"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpnConcentratorsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.gvcd_max_results
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.vpn_concentrator_id_string_list


class DescribeVpnConcentratorsRequest(TypedDict):
    vpn_concentrator_ids: NotRequired[
        "aws_sdk_ec2.types.vpn_concentrator_id_string_list.VpnConcentratorIdStringList"
    ]
    """<p>One or more VPN concentrator IDs.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters to limit the results.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.gvcd_max_results.GVCDMaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
