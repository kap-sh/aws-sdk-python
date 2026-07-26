"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_pool_id


class DeleteIpamPoolRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the pool to delete.</p>"""
    cascade: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Enables you to quickly delete an IPAM pool and all resources within that pool, including provisioned CIDRs, allocations, and other pools.</p> <important> <p>You can only use this option to delete pools in the private scope or pools in the public scope with a source resource. A source resource is a resource used to provision CIDRs to a resource planning pool.</p> </important>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamPoolRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_pool_id" in value:
        pairs.append((f"{prefix}.IpamPoolId", str(value["ipam_pool_id"])))
    if "cascade" in value:
        pairs.append((f"{prefix}.Cascade", "true" if value["cascade"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteIpamPoolRequest:
    out: DeleteIpamPoolRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_pool_id = el.find("IpamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_cascade = el.find("Cascade")
    if child_cascade is not None:
        out["cascade"] = (child_cascade.text or "").lower() == "true"
    return out
