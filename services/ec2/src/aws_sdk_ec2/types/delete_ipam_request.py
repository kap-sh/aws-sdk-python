"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_id


class DeleteIpamRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM to delete.</p>"""
    cascade: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Enables you to quickly delete an IPAM, private scopes, pools in private scopes, and any allocations in the pools in private scopes. You cannot delete the IPAM with this option if there is a pool in your public scope. If you use this option, IPAM does the following:</p> <ul> <li> <p>Deallocates any CIDRs allocated to VPC resources (such as VPCs) in pools in private scopes.</p> <note> <p>No VPC resources are deleted as a result of enabling this option. The CIDR associated with the resource will no longer be allocated from an IPAM pool, but the CIDR itself will remain unchanged.</p> </note> </li> <li> <p>Deprovisions all IPv4 CIDRs provisioned to IPAM pools in private scopes.</p> </li> <li> <p>Deletes all IPAM pools in private scopes.</p> </li> <li> <p>Deletes all non-default private scopes in the IPAM.</p> </li> <li> <p>Deletes the default public and private scopes and the IPAM.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_id" in value:
        pairs.append((f"{prefix}.IpamId", str(value["ipam_id"])))
    if "cascade" in value:
        pairs.append((f"{prefix}.Cascade", "true" if value["cascade"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteIpamRequest:
    out: DeleteIpamRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_cascade = el.find("Cascade")
    if child_cascade is not None:
        out["cascade"] = (child_cascade.text or "").lower() == "true"
    return out
