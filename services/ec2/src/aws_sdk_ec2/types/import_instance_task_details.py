"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceTaskDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_instance_volume_detail_set
    import aws_sdk_ec2.types.platform_values
    import aws_sdk_ec2.types.string


class ImportInstanceTaskDetails(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description of the task.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    platform: NotRequired["aws_sdk_ec2.types.platform_values.PlatformValues"]
    """<p>The instance operating system.</p>"""
    volumes: NotRequired[
        "aws_sdk_ec2.types.import_instance_volume_detail_set.ImportInstanceVolumeDetailSet"
    ]
    """<p>The volumes.</p>"""
