"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRegionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.region_list


class DescribeRegionsResult(TypedDict):
    regions: NotRequired["aws_sdk_ec2.types.region_list.RegionList"]
    """<p>Information about the Regions.</p>"""
