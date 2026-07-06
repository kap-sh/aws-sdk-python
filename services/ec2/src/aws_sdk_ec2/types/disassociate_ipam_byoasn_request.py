"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateIpamByoasnRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class DisassociateIpamByoasnRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    asn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A public 2-byte or 4-byte ASN.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A BYOIP CIDR.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateIpamByoasnRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "asn" in value:
        pairs.append((f"{prefix}.Asn", str(value["asn"])))
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))


def deserialize_ec2_query(el: Element) -> DisassociateIpamByoasnRequest:
    out: DisassociateIpamByoasnRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_asn = el.find("Asn")
    if child_asn is not None:
        out["asn"] = str(child_asn.text or "")
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    return out
