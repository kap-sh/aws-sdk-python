"""Generated from Smithy shape ``com.amazonaws.ec2#BlockDeviceMappingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ebs_block_device_response
    import capo_ec2.types.string


class BlockDeviceMappingResponse(TypedDict, closed=True):
    device_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The device name (for example, <code>/dev/sdh</code> or <code>xvdh</code>).</p>"""
    virtual_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The virtual device name.</p>"""
    ebs: NotRequired["capo_ec2.types.ebs_block_device_response.EbsBlockDeviceResponse"]
    """<p>Parameters used to automatically set up EBS volumes when the instance is launched.</p>"""
    no_device: NotRequired["capo_ec2.types.string.String"]
    """<p>Suppresses the specified device included in the block device mapping.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BlockDeviceMappingResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "device_name" in value:
        pairs.append((f"{prefix}.DeviceName", str(value["device_name"])))
    if "virtual_name" in value:
        pairs.append((f"{prefix}.VirtualName", str(value["virtual_name"])))
    if "ebs" in value:
        import capo_ec2.types.ebs_block_device_response

        capo_ec2.types.ebs_block_device_response.serialize_ec2_query(
            value["ebs"], pairs, f"{prefix}.Ebs"
        )
    if "no_device" in value:
        pairs.append((f"{prefix}.NoDevice", str(value["no_device"])))


def deserialize_ec2_query(el: Element) -> BlockDeviceMappingResponse:
    out: BlockDeviceMappingResponse = {}  # type: ignore[typeddict-item]
    child_device_name = el.find("DeviceName")
    if child_device_name is not None:
        out["device_name"] = str(child_device_name.text or "")
    child_virtual_name = el.find("VirtualName")
    if child_virtual_name is not None:
        out["virtual_name"] = str(child_virtual_name.text or "")
    child_ebs = el.find("Ebs")
    if child_ebs is not None:
        import capo_ec2.types.ebs_block_device_response

        out["ebs"] = capo_ec2.types.ebs_block_device_response.deserialize_ec2_query(
            child_ebs
        )
    child_no_device = el.find("NoDevice")
    if child_no_device is not None:
        out["no_device"] = str(child_no_device.text or "")
    return out
