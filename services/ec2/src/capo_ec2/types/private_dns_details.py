"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class PrivateDnsDetails(TypedDict, closed=True):
    private_dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The private DNS name assigned to the VPC endpoint service.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrivateDnsDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "private_dns_name" in value:
        pairs.append((f"{key_prefix}PrivateDnsName", str(value["private_dns_name"])))


def deserialize_ec2_query(el: Element) -> PrivateDnsDetails:
    out: PrivateDnsDetails = {}  # type: ignore[typeddict-item]
    child_private_dns_name = el.find("PrivateDnsName")
    if child_private_dns_name is not None:
        out["private_dns_name"] = str(child_private_dns_name.text or "")
    return out
