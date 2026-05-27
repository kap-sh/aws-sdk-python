"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceImageMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_instance_image_metadata_max_results
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.instance_id_string_list
    import aws_sdk_ec2.types.string


class DescribeInstanceImageMetadataRequest(TypedDict):
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The name of the Availability Zone (for example, <code>us-west-2a</code>) or Local Zone (for example, <code>us-west-2-lax-1b</code>) of the instance.</p> </li> <li> <p> <code>instance-id</code> - The ID of the instance.</p> </li> <li> <p> <code>image-allowed</code> - A Boolean that indicates whether the image meets the criteria specified for Allowed AMIs.</p> </li> <li> <p> <code>instance-state-name</code> - The state of the instance (<code>pending</code> | <code>running</code> | <code>shutting-down</code> | <code>terminated</code> | <code>stopping</code> | <code>stopped</code>).</p> </li> <li> <p> <code>instance-type</code> - The type of instance (for example, <code>t3.micro</code>).</p> </li> <li> <p> <code>launch-time</code> - The time when the instance was launched, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), for example, <code>2023-09-29T11:04:43.305Z</code>. You can use a wildcard (<code>*</code>), for example, <code>2023-09-29T*</code>, which matches an entire day.</p> </li> <li> <p> <code>owner-alias</code> - The owner alias (<code>amazon</code> | <code>aws-marketplace</code> | <code>aws-backup-vault</code>). The valid aliases are defined in an Amazon-maintained list. This is not the Amazon Web Services account alias that can be set using the IAM console. We recommend that you use the <code>Owner</code> request parameter instead of this filter.</p> </li> <li> <p> <code>owner-id</code> - The Amazon Web Services account ID of the owner. We recommend that you use the <code>Owner</code> request parameter instead of this filter.</p> </li> <li> <p> <code>tag:<key></code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>zone-id</code> - The ID of the Availability Zone (for example, <code>usw2-az2</code>) or Local Zone (for example, <code>usw2-lax1-az1</code>) of the instance.</p> </li> </ul>"""
    instance_ids: NotRequired[
        "aws_sdk_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The instance IDs.</p> <p>If you don't specify an instance ID or filters, the output includes information for all instances.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_instance_image_metadata_max_results.DescribeInstanceImageMetadataMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p> <p>Default: 1000</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
