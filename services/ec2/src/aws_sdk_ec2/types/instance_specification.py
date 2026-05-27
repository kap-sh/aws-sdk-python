"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_id_with_volume_resolver
    import aws_sdk_ec2.types.volume_id_string_list


class InstanceSpecification(TypedDict):
    instance_id: NotRequired[
        "aws_sdk_ec2.types.instance_id_with_volume_resolver.InstanceIdWithVolumeResolver"
    ]
    """<p>The instance to specify which volumes should be snapshotted.</p>"""
    exclude_boot_volume: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Excludes the root volume from being snapshotted.</p>"""
    exclude_data_volume_ids: NotRequired[
        "aws_sdk_ec2.types.volume_id_string_list.VolumeIdStringList"
    ]
    """<p>The IDs of the data (non-root) volumes to exclude from the multi-volume snapshot set. If you specify the ID of the root volume, the request fails. To exclude the root volume, use <b>ExcludeBootVolume</b>.</p> <p>You can specify up to 40 volume IDs per request.</p>"""
