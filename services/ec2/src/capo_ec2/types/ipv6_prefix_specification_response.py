"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6PrefixSpecificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class Ipv6PrefixSpecificationResponse(TypedDict, closed=True):
    ipv6_prefix: NotRequired["capo_ec2.types.string.String"]
    """<p>The IPv6 delegated prefixes assigned to the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6PrefixSpecificationResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv6_prefix" in value:
        pairs.append((f"{prefix}.Ipv6Prefix", str(value["ipv6_prefix"])))


def deserialize_ec2_query(el: Element) -> Ipv6PrefixSpecificationResponse:
    out: Ipv6PrefixSpecificationResponse = {}  # type: ignore[typeddict-item]
    child_ipv6_prefix = el.find("Ipv6Prefix")
    if child_ipv6_prefix is not None:
        out["ipv6_prefix"] = str(child_ipv6_prefix.text or "")
    return out
