"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeDhcpOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_dhcp_options_max_results
    import aws_sdk_ec2.types.dhcp_options_id_string_list
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.string


class DescribeDhcpOptionsRequest(TypedDict):
    dhcp_options_ids: NotRequired[
        "aws_sdk_ec2.types.dhcp_options_id_string_list.DhcpOptionsIdStringList"
    ]
    """<p>The IDs of DHCP option sets.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_dhcp_options_max_results.DescribeDhcpOptionsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>dhcp-options-id</code> - The ID of a DHCP options set.</p> </li> <li> <p> <code>key</code> - The key for one of the options (for example, <code>domain-name</code>).</p> </li> <li> <p> <code>value</code> - The value for one of the options.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the DHCP options set.</p> </li> <li> <p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
