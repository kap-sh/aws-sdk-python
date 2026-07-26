"""Generated from Smithy shape ``com.amazonaws.ec2#DnsEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class DnsEntry(TypedDict, closed=True):
    dns_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The DNS name.</p>"""
    hosted_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the private hosted zone.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DnsEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dns_name" in value:
        pairs.append((f"{prefix}.DnsName", str(value["dns_name"])))
    if "hosted_zone_id" in value:
        pairs.append((f"{prefix}.HostedZoneId", str(value["hosted_zone_id"])))


def deserialize_ec2_query(el: Element) -> DnsEntry:
    out: DnsEntry = {}  # type: ignore[typeddict-item]
    child_dns_name = el.find("DnsName")
    if child_dns_name is not None:
        out["dns_name"] = str(child_dns_name.text or "")
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    return out
