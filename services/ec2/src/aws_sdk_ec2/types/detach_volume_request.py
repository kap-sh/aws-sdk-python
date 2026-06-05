"""Generated from Smithy shape ``com.amazonaws.ec2#DetachVolumeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DetachVolumeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "device" in value:
        pairs.append((f"{prefix}.Device", str(value["device"])))
    if "force" in value:
        pairs.append((f"{prefix}.Force", "true" if value["force"] else "false"))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "volume_id" in value:
        pairs.append((f"{prefix}.VolumeId", str(value["volume_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DetachVolumeRequest:
    out: DetachVolumeRequest = {}  # type: ignore[typeddict-item]
    child_device = el.find("Device")
    if child_device is not None:
        out["device"] = str(child_device.text or "")
    child_force = el.find("Force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
