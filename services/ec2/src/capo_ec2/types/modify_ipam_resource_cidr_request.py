"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamResourceCidrRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_scope_id
    import capo_ec2.types.string


class ModifyIpamResourceCidrRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the resource you want to modify.</p>"""
    resource_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The CIDR of the resource you want to modify.</p>"""
    resource_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the resource you want to modify.</p>"""
    current_ipam_scope_id: NotRequired["capo_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the current scope that the resource CIDR is in.</p>"""
    destination_ipam_scope_id: NotRequired["capo_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the scope you want to transfer the resource CIDR to.</p>"""
    monitored: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Determines if the resource is monitored by IPAM. If a resource is monitored, the resource is discovered by IPAM and you can view details about the resource’s CIDR.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamResourceCidrRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "resource_cidr" in value:
        pairs.append((f"{key_prefix}ResourceCidr", str(value["resource_cidr"])))
    if "resource_region" in value:
        pairs.append((f"{key_prefix}ResourceRegion", str(value["resource_region"])))
    if "current_ipam_scope_id" in value:
        pairs.append(
            (f"{key_prefix}CurrentIpamScopeId", str(value["current_ipam_scope_id"]))
        )
    if "destination_ipam_scope_id" in value:
        pairs.append(
            (
                f"{key_prefix}DestinationIpamScopeId",
                str(value["destination_ipam_scope_id"]),
            )
        )
    if "monitored" in value:
        pairs.append(
            (f"{key_prefix}Monitored", "true" if value["monitored"] else "false")
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamResourceCidrRequest:
    out: ModifyIpamResourceCidrRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_cidr = el.find("ResourceCidr")
    if child_resource_cidr is not None:
        out["resource_cidr"] = str(child_resource_cidr.text or "")
    child_resource_region = el.find("ResourceRegion")
    if child_resource_region is not None:
        out["resource_region"] = str(child_resource_region.text or "")
    child_current_ipam_scope_id = el.find("CurrentIpamScopeId")
    if child_current_ipam_scope_id is not None:
        out["current_ipam_scope_id"] = str(child_current_ipam_scope_id.text or "")
    child_destination_ipam_scope_id = el.find("DestinationIpamScopeId")
    if child_destination_ipam_scope_id is not None:
        out["destination_ipam_scope_id"] = str(
            child_destination_ipam_scope_id.text or ""
        )
    child_monitored = el.find("Monitored")
    if child_monitored is not None:
        out["monitored"] = (child_monitored.text or "").lower() == "true"
    return out
