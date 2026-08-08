"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkAclEntryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.network_acl_id


class DeleteNetworkAclEntryRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_acl_id: NotRequired["capo_ec2.types.network_acl_id.NetworkAclId"]
    """<p>The ID of the network ACL.</p>"""
    rule_number: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The rule number of the entry to delete.</p>"""
    egress: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the rule is an egress rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteNetworkAclEntryRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "network_acl_id" in value:
        pairs.append((f"{key_prefix}NetworkAclId", str(value["network_acl_id"])))
    if "rule_number" in value:
        pairs.append((f"{key_prefix}RuleNumber", str(value["rule_number"])))
    if "egress" in value:
        pairs.append((f"{key_prefix}Egress", "true" if value["egress"] else "false"))


def deserialize_ec2_query(el: Element) -> DeleteNetworkAclEntryRequest:
    out: DeleteNetworkAclEntryRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_network_acl_id = el.find("networkAclId")
    if child_network_acl_id is not None:
        out["network_acl_id"] = str(child_network_acl_id.text or "")
    child_rule_number = el.find("ruleNumber")
    if child_rule_number is not None:
        out["rule_number"] = int(child_rule_number.text or "")
    child_egress = el.find("egress")
    if child_egress is not None:
        out["egress"] = (child_egress.text or "").lower() == "true"
    return out
