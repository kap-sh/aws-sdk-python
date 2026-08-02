"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPoolAllocationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_pool_allocation_id
    import capo_ec2.types.string


class ModifyIpamPoolAllocationRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_pool_allocation_id: NotRequired[
        "capo_ec2.types.ipam_pool_allocation_id.IpamPoolAllocationId"
    ]
    """<p>The ID of the IPAM pool allocation you want to modify.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The new description for the IPAM pool allocation. If you submit a <code>null</code> value, the description is removed from the allocation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamPoolAllocationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_pool_allocation_id" in value:
        pairs.append(
            (f"{key_prefix}IpamPoolAllocationId", str(value["ipam_pool_allocation_id"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))


def deserialize_ec2_query(el: Element) -> ModifyIpamPoolAllocationRequest:
    out: ModifyIpamPoolAllocationRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_pool_allocation_id = el.find("IpamPoolAllocationId")
    if child_ipam_pool_allocation_id is not None:
        out["ipam_pool_allocation_id"] = str(child_ipam_pool_allocation_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
