"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpcResourcesBlockingEncryptionEnforcementRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.get_vpc_resources_blocking_encryption_enforcement_max_results
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_id


class GetVpcResourcesBlockingEncryptionEnforcementRequest(TypedDict):
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC to check for resources blocking encryption enforcement.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.get_vpc_resources_blocking_encryption_enforcement_max_results.GetVpcResourcesBlockingEncryptionEnforcementMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
