"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.disk_image_list
    import aws_sdk_ec2.types.import_instance_launch_specification
    import aws_sdk_ec2.types.platform_values
    import aws_sdk_ec2.types.string


class ImportInstanceRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the instance being imported.</p>"""
    launch_specification: NotRequired[
        "aws_sdk_ec2.types.import_instance_launch_specification.ImportInstanceLaunchSpecification"
    ]
    """<p>The launch specification.</p>"""
    disk_images: NotRequired["aws_sdk_ec2.types.disk_image_list.DiskImageList"]
    """<p>The disk image.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.platform_values.PlatformValues"]
    """<p>The instance operating system.</p>"""
