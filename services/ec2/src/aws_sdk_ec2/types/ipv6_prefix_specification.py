"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6PrefixSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class Ipv6PrefixSpecification(TypedDict):
    ipv6_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 prefix.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6PrefixSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv6_prefix" in value:
        pairs.append((f"{prefix}.Ipv6Prefix", str(value["ipv6_prefix"])))


def deserialize_ec2_query(el: Element) -> Ipv6PrefixSpecification:
    out: Ipv6PrefixSpecification = {}  # type: ignore[typeddict-item]
    child_ipv6_prefix = el.find("Ipv6Prefix")
    if child_ipv6_prefix is not None:
        out["ipv6_prefix"] = str(child_ipv6_prefix.text or "")
    return out
