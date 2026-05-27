"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeHostsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.request_host_id_list
    import aws_sdk_ec2.types.string


class DescribeHostsRequest(TypedDict):
    host_ids: NotRequired["aws_sdk_ec2.types.request_host_id_list.RequestHostIdList"]
    """<p>The IDs of the Dedicated Hosts. The IDs are used for targeted instance launches.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned <code>nextToken</code> value. This value can be between 5 and 500. If <code>maxResults</code> is given a larger value than 500, you receive an error.</p> <p>You cannot specify this parameter and the host IDs parameter in the same request.</p>"""
    filter: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>auto-placement</code> - Whether auto-placement is enabled or disabled (<code>on</code> | <code>off</code>).</p> </li> <li> <p> <code>availability-zone</code> - The Availability Zone of the host.</p> </li> <li> <p> <code>client-token</code> - The idempotency token that you provided when you allocated the host.</p> </li> <li> <p> <code>host-reservation-id</code> - The ID of the reservation assigned to this host.</p> </li> <li> <p> <code>instance-type</code> - The instance type size that the Dedicated Host is configured to support.</p> </li> <li> <p> <code>state</code> - The allocation state of the Dedicated Host (<code>available</code> | <code>under-assessment</code> | <code>permanent-failure</code> | <code>released</code> | <code>released-permanent-failure</code>).</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> </ul>"""
