"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFpgaImagesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_fpga_images_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.fpga_image_id_list
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.owner_string_list


class DescribeFpgaImagesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    fpga_image_ids: NotRequired["aws_sdk_ec2.types.fpga_image_id_list.FpgaImageIdList"]
    """<p>The AFI IDs.</p>"""
    owners: NotRequired["aws_sdk_ec2.types.owner_string_list.OwnerStringList"]
    """<p>Filters the AFI by owner. Specify an Amazon Web Services account ID, <code>self</code> (owner is the sender of the request), or an Amazon Web Services owner alias (valid values are <code>amazon</code> | <code>aws-marketplace</code>).</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>create-time</code> - The creation time of the AFI.</p> </li> <li> <p> <code>fpga-image-id</code> - The FPGA image identifier (AFI ID).</p> </li> <li> <p> <code>fpga-image-global-id</code> - The global FPGA image identifier (AGFI ID).</p> </li> <li> <p> <code>name</code> - The name of the AFI.</p> </li> <li> <p> <code>owner-id</code> - The Amazon Web Services account ID of the AFI owner.</p> </li> <li> <p> <code>product-code</code> - The product code.</p> </li> <li> <p> <code>shell-version</code> - The version of the Amazon Web Services Shell that was used to create the bitstream.</p> </li> <li> <p> <code>state</code> - The state of the AFI (<code>pending</code> | <code>failed</code> | <code>available</code> | <code>unavailable</code>).</p> </li> <li> <p> <code>tag</code>:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>update-time</code> - The time of the most recent update.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_fpga_images_max_results.DescribeFpgaImagesMaxResults"
    ]
    """<p>The maximum number of results to return in a single call.</p>"""
