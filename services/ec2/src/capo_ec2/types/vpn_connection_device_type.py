"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnectionDeviceType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class VpnConnectionDeviceType(TypedDict, closed=True):
    vpn_connection_device_type_id: NotRequired["capo_ec2.types.string.String"]
    """<p>Customer gateway device identifier.</p>"""
    vendor: NotRequired["capo_ec2.types.string.String"]
    """<p>Customer gateway device vendor.</p>"""
    platform: NotRequired["capo_ec2.types.string.String"]
    """<p>Customer gateway device platform.</p>"""
    software: NotRequired["capo_ec2.types.string.String"]
    """<p>Customer gateway device software version.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnConnectionDeviceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpn_connection_device_type_id" in value:
        pairs.append(
            (
                f"{prefix}.VpnConnectionDeviceTypeId",
                str(value["vpn_connection_device_type_id"]),
            )
        )
    if "vendor" in value:
        pairs.append((f"{prefix}.Vendor", str(value["vendor"])))
    if "platform" in value:
        pairs.append((f"{prefix}.Platform", str(value["platform"])))
    if "software" in value:
        pairs.append((f"{prefix}.Software", str(value["software"])))


def deserialize_ec2_query(el: Element) -> VpnConnectionDeviceType:
    out: VpnConnectionDeviceType = {}  # type: ignore[typeddict-item]
    child_vpn_connection_device_type_id = el.find("VpnConnectionDeviceTypeId")
    if child_vpn_connection_device_type_id is not None:
        out["vpn_connection_device_type_id"] = str(
            child_vpn_connection_device_type_id.text or ""
        )
    child_vendor = el.find("Vendor")
    if child_vendor is not None:
        out["vendor"] = str(child_vendor.text or "")
    child_platform = el.find("Platform")
    if child_platform is not None:
        out["platform"] = str(child_platform.text or "")
    child_software = el.find("Software")
    if child_software is not None:
        out["software"] = str(child_software.text or "")
    return out
