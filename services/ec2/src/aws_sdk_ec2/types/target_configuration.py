"""Generated from Smithy shape ``com.amazonaws.ec2#TargetConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class TargetConfiguration(TypedDict):
    instance_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of instances the Convertible Reserved Instance offering can be applied to. This parameter is reserved and cannot be specified in a request</p>"""
    offering_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Convertible Reserved Instance offering.</p>"""
