"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeMacHostsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_mac_hosts_request_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.request_host_id_list
    import aws_sdk_ec2.types.string


class DescribeMacHostsRequest(TypedDict):
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone of the EC2 Mac Dedicated Host.</p> </li> <li> <p> <code>instance-type</code> - The instance type size that the EC2 Mac Dedicated Host is configured to support.</p> </li> </ul>"""
    host_ids: NotRequired["aws_sdk_ec2.types.request_host_id_list.RequestHostIdList"]
    """<p> The IDs of the EC2 Mac Dedicated Hosts. </p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_mac_hosts_request_max_results.DescribeMacHostsRequestMaxResults"
    ]
    """<p>The maximum number of results to return for the request in a single page. The remaining results can be seen by sending another request with the returned <code>nextToken</code> value. This value can be between 5 and 500. If <code>maxResults</code> is given a larger value than 500, you receive an error.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
