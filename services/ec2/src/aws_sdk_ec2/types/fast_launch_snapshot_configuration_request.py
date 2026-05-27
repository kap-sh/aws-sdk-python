"""Generated from Smithy shape ``com.amazonaws.ec2#FastLaunchSnapshotConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class FastLaunchSnapshotConfigurationRequest(TypedDict):
    target_resource_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of pre-provisioned snapshots to keep on hand for a Windows fast launch enabled AMI.</p>"""
