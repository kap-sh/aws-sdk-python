"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySecurityGroupRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.security_group_id
    import capo_ec2.types.security_group_rule_update_list


class ModifySecurityGroupRulesRequest(TypedDict, closed=True):
    group_id: NotRequired["capo_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group.</p>"""
    security_group_rules: NotRequired[
        "capo_ec2.types.security_group_rule_update_list.SecurityGroupRuleUpdateList"
    ]
    """<p>Information about the security group properties to update.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifySecurityGroupRulesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "security_group_rules" in value:
        import capo_ec2.types.security_group_rule_update_list

        capo_ec2.types.security_group_rule_update_list.serialize_ec2_query(
            value["security_group_rules"], pairs, f"{key_prefix}SecurityGroupRules"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifySecurityGroupRulesRequest:
    out: ModifySecurityGroupRulesRequest = {}  # type: ignore[typeddict-item]
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    if el.find("SecurityGroupRules") is not None:
        import capo_ec2.types.security_group_rule_update_list

        out["security_group_rules"] = (
            capo_ec2.types.security_group_rule_update_list.deserialize_ec2_query(
                el, "SecurityGroupRules"
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
