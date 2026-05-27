"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeImageUsageReportEntriesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.describe_image_usage_report_entries_max_results
    import aws_sdk_ec2.types.describe_image_usage_reports_image_id_string_list
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.image_usage_report_id_string_list
    import aws_sdk_ec2.types.string


class DescribeImageUsageReportEntriesRequest(TypedDict):
    image_ids: NotRequired[
        "aws_sdk_ec2.types.describe_image_usage_reports_image_id_string_list.DescribeImageUsageReportsImageIdStringList"
    ]
    """<p>The IDs of the images for filtering the report entries. If specified, only report entries containing these images are returned.</p>"""
    report_ids: NotRequired[
        "aws_sdk_ec2.types.image_usage_report_id_string_list.ImageUsageReportIdStringList"
    ]
    """<p>The IDs of the usage reports.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>account-id</code> - A 12-digit Amazon Web Services account ID.</p> </li> <li> <p> <code>creation-time</code> - The time when the report was created, in the ISO 8601 format in the UTC time zone (YYYY-MM-DDThh:mm:ss.sssZ), for example, <code>2025-11-29T11:04:43.305Z</code>. You can use a wildcard (<code>*</code>), for example, <code>2025-11-29T*</code>, which matches an entire day.</p> </li> <li> <p> <code>resource-type</code> - The resource type (<code>ec2:Instance</code> | <code>ec2:LaunchTemplate</code>).</p> </li> </ul>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.describe_image_usage_report_entries_max_results.DescribeImageUsageReportEntriesMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination\">Pagination</a>.</p>"""
