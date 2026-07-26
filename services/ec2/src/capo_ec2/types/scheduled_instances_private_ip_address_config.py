"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesPrivateIpAddressConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string


class ScheduledInstancesPrivateIpAddressConfig(TypedDict, closed=True):
    primary: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this is a primary IPv4 address. Otherwise, this is a secondary IPv4 address.</p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv4 address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesPrivateIpAddressConfig,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "primary" in value:
        pairs.append((f"{prefix}.Primary", "true" if value["primary"] else "false"))
    if "private_ip_address" in value:
        pairs.append((f"{prefix}.PrivateIpAddress", str(value["private_ip_address"])))


def deserialize_ec2_query(el: Element) -> ScheduledInstancesPrivateIpAddressConfig:
    out: ScheduledInstancesPrivateIpAddressConfig = {}  # type: ignore[typeddict-item]
    child_primary = el.find("Primary")
    if child_primary is not None:
        out["primary"] = (child_primary.text or "").lower() == "true"
    child_private_ip_address = el.find("PrivateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    return out
