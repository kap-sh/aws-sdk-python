"""Generated from Smithy shape ``com.amazonaws.ec2#ReleaseIpamPoolAllocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_pool_allocation_id
    import capo_ec2.types.ipam_pool_id
    import capo_ec2.types.string


class ReleaseIpamPoolAllocationRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the IPAM pool which contains the allocation you want to release.</p>"""
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR of the allocation you want to release.</p>"""
    ipam_pool_allocation_id: NotRequired[
        "capo_ec2.types.ipam_pool_allocation_id.IpamPoolAllocationId"
    ]
    """<p>The ID of the allocation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReleaseIpamPoolAllocationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_pool_id" in value:
        pairs.append((f"{prefix}.IpamPoolId", str(value["ipam_pool_id"])))
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))
    if "ipam_pool_allocation_id" in value:
        pairs.append(
            (f"{prefix}.IpamPoolAllocationId", str(value["ipam_pool_allocation_id"]))
        )


def deserialize_ec2_query(el: Element) -> ReleaseIpamPoolAllocationRequest:
    out: ReleaseIpamPoolAllocationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_pool_id = el.find("IpamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_ipam_pool_allocation_id = el.find("IpamPoolAllocationId")
    if child_ipam_pool_allocation_id is not None:
        out["ipam_pool_allocation_id"] = str(child_ipam_pool_allocation_id.text or "")
    return out
