"""Generated from Smithy shape ``com.amazonaws.ec2#DetachVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_id_for_resolver
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_id_with_resolver


class DetachVolumeRequest(TypedDict):
    device: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name.</p>"""
    force: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Forces detachment if the previous detachment attempt did not occur cleanly (for example, logging into an instance, unmounting the volume, and detaching normally). This option can lead to data loss or a corrupted file system. Use this option only as a last resort to detach a volume from a failed instance. The instance won't have an opportunity to flush file system caches or file system metadata. If you use this option, you must perform file system check and repair procedures.</p>"""
    instance_id: NotRequired[
        "aws_sdk_ec2.types.instance_id_for_resolver.InstanceIdForResolver"
    ]
    """<p>The ID of the instance. If you are detaching a Multi-Attach enabled volume, you must specify an instance ID.</p>"""
    volume_id: NotRequired[
        "aws_sdk_ec2.types.volume_id_with_resolver.VolumeIdWithResolver"
    ]
    """<p>The ID of the volume.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
