"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRegionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.region_name_string_list


class DescribeRegionsRequest(TypedDict):
    region_names: NotRequired[
        "aws_sdk_ec2.types.region_name_string_list.RegionNameStringList"
    ]
    """<p>The names of the Regions. You can specify any Regions, whether they are enabled and disabled for your account.</p>"""
    all_regions: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to display all Regions, including Regions that are disabled for your account.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>endpoint</code> - The endpoint of the Region (for example, <code>ec2.us-east-1.amazonaws.com</code>).</p> </li> <li> <p> <code>opt-in-status</code> - The opt-in status of the Region (<code>opt-in-not-required</code> | <code>opted-in</code> | <code>not-opted-in</code>).</p> </li> <li> <p> <code>region-name</code> - The name of the Region (for example, <code>us-east-1</code>).</p> </li> </ul>"""
