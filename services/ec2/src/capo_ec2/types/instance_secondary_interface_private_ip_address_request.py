"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfacePrivateIpAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class InstanceSecondaryInterfacePrivateIpAddressRequest(TypedDict, closed=True):
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The private IPv4 address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceSecondaryInterfacePrivateIpAddressRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "private_ip_address" in value:
        pairs.append((f"{prefix}.PrivateIpAddress", str(value["private_ip_address"])))


def deserialize_ec2_query(
    el: Element,
) -> InstanceSecondaryInterfacePrivateIpAddressRequest:
    out: InstanceSecondaryInterfacePrivateIpAddressRequest = {}  # type: ignore[typeddict-item]
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    return out
