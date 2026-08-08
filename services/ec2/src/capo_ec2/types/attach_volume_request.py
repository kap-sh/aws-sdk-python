"""Generated from Smithy shape ``com.amazonaws.ec2#AttachVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.boxed_integer
    import capo_ec2.types.instance_id
    import capo_ec2.types.string
    import capo_ec2.types.volume_id


class AttachVolumeRequest(TypedDict, closed=True):
    device: NotRequired["capo_ec2.types.string.String"]
    """<p>The device name (for example, <code>/dev/sdh</code> or <code>xvdh</code>).</p>"""
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    volume_id: NotRequired["capo_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the EBS volume. The volume and instance must be within the same Availability Zone.</p>"""
    ebs_card_index: NotRequired["capo_ec2.types.boxed_integer.BoxedInteger"]
    """<p>The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttachVolumeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "device" in value:
        pairs.append((f"{key_prefix}Device", str(value["device"])))
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))
    if "ebs_card_index" in value:
        pairs.append((f"{key_prefix}EbsCardIndex", str(value["ebs_card_index"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> AttachVolumeRequest:
    out: AttachVolumeRequest = {}  # type: ignore[typeddict-item]
    child_device = el.find("Device")
    if child_device is not None:
        out["device"] = str(child_device.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_ebs_card_index = el.find("EbsCardIndex")
    if child_ebs_card_index is not None:
        out["ebs_card_index"] = int(child_ebs_card_index.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
