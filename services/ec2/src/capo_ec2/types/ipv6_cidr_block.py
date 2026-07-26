"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6CidrBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class Ipv6CidrBlock(TypedDict, closed=True):
    ipv6_cidr_block: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 CIDR block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6CidrBlock, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv6_cidr_block" in value:
        pairs.append((f"{prefix}.Ipv6CidrBlock", str(value["ipv6_cidr_block"])))


def deserialize_ec2_query(el: Element) -> Ipv6CidrBlock:
    out: Ipv6CidrBlock = {}  # type: ignore[typeddict-item]
    child_ipv6_cidr_block = el.find("Ipv6CidrBlock")
    if child_ipv6_cidr_block is not None:
        out["ipv6_cidr_block"] = str(child_ipv6_cidr_block.text or "")
    return out
