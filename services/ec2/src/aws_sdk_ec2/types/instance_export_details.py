"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceExportDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_environment
    import aws_sdk_ec2.types.string


class InstanceExportDetails(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the resource being exported.</p>"""
    target_environment: NotRequired[
        "aws_sdk_ec2.types.export_environment.ExportEnvironment"
    ]
    """<p>The target virtualization environment.</p>"""
