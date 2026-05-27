"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEndpointServicesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class DescribeVpcEndpointServicesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    service_names: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The service names.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>owner</code> - The ID or alias of the Amazon Web Services account that owns the service.</p> </li> <li> <p> <code>service-name</code> - The name of the service.</p> </li> <li> <p> <code>service-region</code> - The Region of the service.</p> </li> <li> <p> <code>service-type</code> - The type of service (<code>Interface</code> | <code>Gateway</code> | <code>GatewayLoadBalancer</code>).</p> </li> <li> <p> <code>supported-ip-address-types</code> - The IP address type (<code>ipv4</code> | <code>ipv6</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. The request returns a token that you can specify in a subsequent call to get the next set of results.</p> <p>Constraint: If the value is greater than 1,000, we return only 1,000 items.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next set of items to return. (You received this token from a prior call.)</p>"""
    service_regions: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The service Regions.</p>"""
