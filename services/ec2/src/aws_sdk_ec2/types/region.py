"""Generated from Smithy shape ``com.amazonaws.ec2#Region``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.region_geography_list
    import aws_sdk_ec2.types.string


class Region(TypedDict):
    opt_in_status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region opt-in status. The possible values are <code>opt-in-not-required</code>, <code>opted-in</code>, and <code>not-opted-in</code>.</p>"""
    geography: NotRequired[
        "aws_sdk_ec2.types.region_geography_list.RegionGeographyList"
    ]
    """<p>The geography information for the Region. The geography is returned as a list.</p>"""
    region_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Region.</p>"""
    endpoint: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region service endpoint.</p>"""
