"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceConnectEndpointsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.instance_connect_endpoint_max_results
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.value_string_list


class DescribeInstanceConnectEndpointsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.instance_connect_endpoint_max_results.InstanceConnectEndpointMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>instance-connect-endpoint-id</code> - The ID of the EC2 Instance Connect Endpoint.</p> </li> <li> <p> <code>state</code> - The state of the EC2 Instance Connect Endpoint (<code>create-in-progress</code> | <code>create-complete</code> | <code>create-failed</code> | <code>delete-in-progress</code> | <code>delete-complete</code> | <code>delete-failed</code>).</p> </li> <li> <p> <code>subnet-id</code> - The ID of the subnet in which the EC2 Instance Connect Endpoint was created.</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>tag-value</code> - The value of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific value, regardless of tag key.</p> </li> <li> <p> <code>vpc-id</code> - The ID of the VPC in which the EC2 Instance Connect Endpoint was created.</p> </li> </ul>"""
    instance_connect_endpoint_ids: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>One or more EC2 Instance Connect Endpoint IDs.</p>"""
