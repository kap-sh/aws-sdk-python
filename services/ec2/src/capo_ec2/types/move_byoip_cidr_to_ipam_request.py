"""Generated from Smithy shape ``com.amazonaws.ec2#MoveByoipCidrToIpamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.string


class MoveByoipCidrToIpamRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The BYOIP CIDR.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The IPAM pool ID.</p>"""
    ipam_pool_owner: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the IPAM pool.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MoveByoipCidrToIpamRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "ipam_pool_id" in value:
        pairs.append((f"{prefix}.IpamPoolId", str(value["ipam_pool_id"])))
    if "ipam_pool_owner" in value:
        pairs.append((f"{prefix}.IpamPoolOwner", str(value["ipam_pool_owner"])))


def deserialize_ec2_query(el: Element) -> MoveByoipCidrToIpamRequest:
    out: MoveByoipCidrToIpamRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_ipam_pool_id = el.find("IpamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_ipam_pool_owner = el.find("IpamPoolOwner")
    if child_ipam_pool_owner is not None:
        out["ipam_pool_owner"] = str(child_ipam_pool_owner.text or "")
    return out
