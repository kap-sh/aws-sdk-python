"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcClassicLinkDnsSupportRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_max_results
    import aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_next_token
    import aws_sdk_ec2.types.vpc_classic_link_id_list


class DescribeVpcClassicLinkDnsSupportRequest(TypedDict):
    vpc_ids: NotRequired[
        "aws_sdk_ec2.types.vpc_classic_link_id_list.VpcClassicLinkIdList"
    ]
    """<p>The IDs of the VPCs.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_max_results.DescribeVpcClassicLinkDnsSupportMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired[
        "aws_sdk_ec2.types.describe_vpc_classic_link_dns_support_next_token.DescribeVpcClassicLinkDnsSupportNextToken"
    ]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
