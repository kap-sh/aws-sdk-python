"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionIpamPoolCidrRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_pool_id
    import aws_sdk_ec2.types.string


class DeprovisionIpamPoolCidrRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the pool that has the CIDR you want to deprovision.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The CIDR which you want to deprovision from the pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeprovisionIpamPoolCidrRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_pool_id" in value:
        pairs.append((f"{prefix}.IpamPoolId", str(value["ipam_pool_id"])))
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))


def deserialize_ec2_query(el: Element) -> DeprovisionIpamPoolCidrRequest:
    out: DeprovisionIpamPoolCidrRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_pool_id = el.find("IpamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    return out
