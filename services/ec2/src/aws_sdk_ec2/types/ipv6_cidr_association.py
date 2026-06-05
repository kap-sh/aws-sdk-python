"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6CidrAssociation``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class Ipv6CidrAssociation(TypedDict):
    ipv6_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR block.</p>"""
    associated_resource: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The resource that's associated with the IPv6 CIDR block.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6CidrAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipv6_cidr" in value:
        pairs.append((f"{prefix}.Ipv6Cidr", str(value["ipv6_cidr"])))
    if "associated_resource" in value:
        pairs.append(
            (f"{prefix}.AssociatedResource", str(value["associated_resource"]))
        )


def deserialize_ec2_query(el: Element) -> Ipv6CidrAssociation:
    out: Ipv6CidrAssociation = {}  # type: ignore[typeddict-item]
    child_ipv6_cidr = el.find("Ipv6Cidr")
    if child_ipv6_cidr is not None:
        out["ipv6_cidr"] = str(child_ipv6_cidr.text or "")
    child_associated_resource = el.find("AssociatedResource")
    if child_associated_resource is not None:
        out["associated_resource"] = str(child_associated_resource.text or "")
    return out
