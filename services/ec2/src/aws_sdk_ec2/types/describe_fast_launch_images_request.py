"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastLaunchImagesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_fast_launch_images_request_max_results
    import aws_sdk_ec2.types.fast_launch_image_id_list
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.next_token


class DescribeFastLaunchImagesRequest(TypedDict):
    image_ids: NotRequired[
        "aws_sdk_ec2.types.fast_launch_image_id_list.FastLaunchImageIdList"
    ]
    """<p>Specify one or more Windows AMI image IDs for the request.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>Use the following filters to streamline results.</p> <ul> <li> <p> <code>resource-type</code> - The resource type for pre-provisioning.</p> </li> <li> <p> <code>owner-id</code> - The owner ID for the pre-provisioning resource.</p> </li> <li> <p> <code>state</code> - The current state of fast launching for the Windows AMI.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_fast_launch_images_request_max_results.DescribeFastLaunchImagesRequestMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
