"""Generated from Smithy shape ``com.amazonaws.ec2#EnableIpamPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ipam_policy_id
    import capo_ec2.types.string


class EnableIpamPolicyRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_policy_id: NotRequired["capo_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy to enable.</p>"""
    organization_target_id: NotRequired["capo_ec2.types.string.String"]
    """<p>A target can be an individual Amazon Web Services account or an entity within an Amazon Web Services Organization to which an IPAM policy can be applied.</p> <p>The ID of the Amazon Web Services Organizations target for which to enable the IPAM policy. This parameter is required only when IPAM is integrated with Amazon Web Services Organizations. When IPAM is not integrated with Amazon Web Services Organizations, omit this parameter and the policy will apply to the current account.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableIpamPolicyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_policy_id" in value:
        pairs.append((f"{key_prefix}IpamPolicyId", str(value["ipam_policy_id"])))
    if "organization_target_id" in value:
        pairs.append(
            (f"{key_prefix}OrganizationTargetId", str(value["organization_target_id"]))
        )


def deserialize_ec2_query(el: Element) -> EnableIpamPolicyRequest:
    out: EnableIpamPolicyRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_policy_id = el.find("IpamPolicyId")
    if child_ipam_policy_id is not None:
        out["ipam_policy_id"] = str(child_ipam_policy_id.text or "")
    child_organization_target_id = el.find("OrganizationTargetId")
    if child_organization_target_id is not None:
        out["organization_target_id"] = str(child_organization_target_id.text or "")
    return out
