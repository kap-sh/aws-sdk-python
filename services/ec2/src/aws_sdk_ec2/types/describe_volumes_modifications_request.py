"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVolumesModificationsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_id_string_list


class DescribeVolumesModificationsRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    volume_ids: NotRequired[
        "aws_sdk_ec2.types.volume_id_string_list.VolumeIdStringList"
    ]
    """<p>The IDs of the volumes.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>modification-state</code> - The current modification state (modifying | optimizing | completed | failed).</p> </li> <li> <p> <code>original-iops</code> - The original IOPS rate of the volume.</p> </li> <li> <p> <code>original-size</code> - The original size of the volume, in GiB.</p> </li> <li> <p> <code>original-volume-type</code> - The original volume type of the volume (standard | io1 | io2 | gp2 | sc1 | st1).</p> </li> <li> <p> <code>originalMultiAttachEnabled</code> - Indicates whether Multi-Attach support was enabled (true | false).</p> </li> <li> <p> <code>start-time</code> - The modification start time.</p> </li> <li> <p> <code>target-iops</code> - The target IOPS rate of the volume.</p> </li> <li> <p> <code>target-size</code> - The target size of the volume, in GiB.</p> </li> <li> <p> <code>target-volume-type</code> - The target volume type of the volume (standard | io1 | io2 | gp2 | sc1 | st1).</p> </li> <li> <p> <code>targetMultiAttachEnabled</code> - Indicates whether Multi-Attach support is to be enabled (true | false).</p> </li> <li> <p> <code>volume-id</code> - The ID of the volume.</p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of results (up to a limit of 500) to be returned in a paginated request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
