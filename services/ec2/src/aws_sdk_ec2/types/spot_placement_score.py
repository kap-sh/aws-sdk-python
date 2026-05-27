"""Generated from Smithy shape ``com.amazonaws.ec2#SpotPlacementScore``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class SpotPlacementScore(TypedDict):
    region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Region.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    score: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The placement score, on a scale from <code>1</code> to <code>10</code>. A score of <code>10</code> indicates that your Spot request is highly likely to succeed in this Region or Availability Zone. A score of <code>1</code> indicates that your Spot request is not likely to succeed. </p>"""
