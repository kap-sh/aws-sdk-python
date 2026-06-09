"""Generated from Smithy shape ``com.amazonaws.ec2#PciId``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PciId(TypedDict):
    device_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the device.</p>"""
    vendor_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the vendor.</p>"""
    subsystem_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the subsystem.</p>"""
    subsystem_vendor_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the vendor for the subsystem.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PciId, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "device_id" in value:
        pairs.append((f"{prefix}.DeviceId", str(value["device_id"])))
    if "vendor_id" in value:
        pairs.append((f"{prefix}.VendorId", str(value["vendor_id"])))
    if "subsystem_id" in value:
        pairs.append((f"{prefix}.SubsystemId", str(value["subsystem_id"])))
    if "subsystem_vendor_id" in value:
        pairs.append((f"{prefix}.SubsystemVendorId", str(value["subsystem_vendor_id"])))


def deserialize_ec2_query(el: Element) -> PciId:
    out: PciId = {}  # type: ignore[typeddict-item]
    child_device_id = el.find("DeviceId")
    if child_device_id is not None:
        out["device_id"] = str(child_device_id.text or "")
    child_vendor_id = el.find("VendorId")
    if child_vendor_id is not None:
        out["vendor_id"] = str(child_vendor_id.text or "")
    child_subsystem_id = el.find("SubsystemId")
    if child_subsystem_id is not None:
        out["subsystem_id"] = str(child_subsystem_id.text or "")
    child_subsystem_vendor_id = el.find("SubsystemVendorId")
    if child_subsystem_vendor_id is not None:
        out["subsystem_vendor_id"] = str(child_subsystem_vendor_id.text or "")
    return out
