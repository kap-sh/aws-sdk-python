"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionPublicIpv4PoolCidrRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipv4_pool_ec2_id
    import capo_ec2.types.string


class DeprovisionPublicIpv4PoolCidrRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    pool_id: NotRequired["capo_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of the pool that you want to deprovision the CIDR from.</p>"""
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR you want to deprovision from the pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeprovisionPublicIpv4PoolCidrRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "pool_id" in value:
        pairs.append((f"{key_prefix}PoolId", str(value["pool_id"])))
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))


def deserialize_ec2_query(el: Element) -> DeprovisionPublicIpv4PoolCidrRequest:
    out: DeprovisionPublicIpv4PoolCidrRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_pool_id = el.find("PoolId")
    if child_pool_id is not None:
        out["pool_id"] = str(child_pool_id.text or "")
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    return out
