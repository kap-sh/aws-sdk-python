"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnConnectionDeviceTypesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.gvcd_max_results
    import aws_sdk_ec2.types.next_token


class GetVpnConnectionDeviceTypesRequest(TypedDict):
    max_results: NotRequired["aws_sdk_ec2.types.gvcd_max_results.GVCDMaxResults"]
    """<p>The maximum number of results returned by <code>GetVpnConnectionDeviceTypes</code> in paginated output. When this parameter is used, <code>GetVpnConnectionDeviceTypes</code> only returns <code>MaxResults</code> results in a single page along with a <code>NextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>GetVpnConnectionDeviceTypes</code> request with the returned <code>NextToken</code> value. This value can be between 200 and 1000. If this parameter is not used, then <code>GetVpnConnectionDeviceTypes</code> returns all results.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The <code>NextToken</code> value returned from a previous paginated <code>GetVpnConnectionDeviceTypes</code> request where <code>MaxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>NextToken</code> value. This value is null when there are no more results to return. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
