"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionIpamByoasnRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.string


class DeprovisionIpamByoasnRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The IPAM ID.</p>"""
    asn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>An ASN.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeprovisionIpamByoasnRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_id" in value:
        pairs.append((f"{prefix}.IpamId", str(value["ipam_id"])))
    if "asn" in value:
        pairs.append((f"{prefix}.Asn", str(value["asn"])))


def deserialize_ec2_query(el: Element) -> DeprovisionIpamByoasnRequest:
    out: DeprovisionIpamByoasnRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_asn = el.find("Asn")
    if child_asn is not None:
        out["asn"] = str(child_asn.text or "")
    return out
