"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateIpAddressSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string


class PrivateIpAddressSpecification(TypedDict, closed=True):
    primary: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the private IPv4 address is the primary private IPv4 address. Only one IPv4 address can be designated as primary.</p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The private IPv4 address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrivateIpAddressSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "primary" in value:
        pairs.append((f"{key_prefix}Primary", "true" if value["primary"] else "false"))
    if "private_ip_address" in value:
        pairs.append(
            (f"{key_prefix}PrivateIpAddress", str(value["private_ip_address"]))
        )


def deserialize_ec2_query(el: Element) -> PrivateIpAddressSpecification:
    out: PrivateIpAddressSpecification = {}  # type: ignore[typeddict-item]
    child_primary = el.find("primary")
    if child_primary is not None:
        out["primary"] = (child_primary.text or "").lower() == "true"
    child_private_ip_address = el.find("privateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    return out
