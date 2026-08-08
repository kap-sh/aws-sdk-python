"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv4Prefix``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class InstanceIpv4Prefix(TypedDict, closed=True):
    ipv4_prefix: NotRequired["capo_ec2.types.string.String"]
    """<p>One or more IPv4 prefixes assigned to the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceIpv4Prefix, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipv4_prefix" in value:
        pairs.append((f"{key_prefix}Ipv4Prefix", str(value["ipv4_prefix"])))


def deserialize_ec2_query(el: Element) -> InstanceIpv4Prefix:
    out: InstanceIpv4Prefix = {}  # type: ignore[typeddict-item]
    child_ipv4_prefix = el.find("ipv4Prefix")
    if child_ipv4_prefix is not None:
        out["ipv4_prefix"] = str(child_ipv4_prefix.text or "")
    return out
