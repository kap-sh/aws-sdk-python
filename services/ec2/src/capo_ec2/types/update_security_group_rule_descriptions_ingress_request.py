"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateSecurityGroupRuleDescriptionsIngressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.ip_permission_list
    import capo_ec2.types.security_group_id
    import capo_ec2.types.security_group_name
    import capo_ec2.types.security_group_rule_description_list


class UpdateSecurityGroupRuleDescriptionsIngressRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    group_id: NotRequired["capo_ec2.types.security_group_id.SecurityGroupId"]
    """<p>The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.</p>"""
    group_name: NotRequired["capo_ec2.types.security_group_name.SecurityGroupName"]
    """<p>[Default VPC] The name of the security group. You must specify either the security group ID or the security group name. For security groups in a nondefault VPC, you must specify the security group ID.</p>"""
    ip_permissions: NotRequired["capo_ec2.types.ip_permission_list.IpPermissionList"]
    """<p>The IP permissions for the security group rule. You must specify either IP permissions or a description.</p>"""
    security_group_rule_descriptions: NotRequired[
        "capo_ec2.types.security_group_rule_description_list.SecurityGroupRuleDescriptionList"
    ]
    """<p>The description for the ingress security group rules. You must specify either a description or IP permissions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UpdateSecurityGroupRuleDescriptionsIngressRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "group_id" in value:
        pairs.append((f"{key_prefix}GroupId", str(value["group_id"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "ip_permissions" in value:
        import capo_ec2.types.ip_permission_list

        capo_ec2.types.ip_permission_list.serialize_ec2_query(
            value["ip_permissions"], pairs, f"{key_prefix}IpPermissions"
        )
    if "security_group_rule_descriptions" in value:
        import capo_ec2.types.security_group_rule_description_list

        capo_ec2.types.security_group_rule_description_list.serialize_ec2_query(
            value["security_group_rule_descriptions"],
            pairs,
            f"{key_prefix}SecurityGroupRuleDescriptions",
        )


def deserialize_ec2_query(
    el: Element,
) -> UpdateSecurityGroupRuleDescriptionsIngressRequest:
    out: UpdateSecurityGroupRuleDescriptionsIngressRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    if el.find("IpPermissions") is not None:
        import capo_ec2.types.ip_permission_list

        out["ip_permissions"] = capo_ec2.types.ip_permission_list.deserialize_ec2_query(
            el, "IpPermissions"
        )
    if el.find("SecurityGroupRuleDescriptions") is not None:
        import capo_ec2.types.security_group_rule_description_list

        out["security_group_rule_descriptions"] = (
            capo_ec2.types.security_group_rule_description_list.deserialize_ec2_query(
                el, "SecurityGroupRuleDescriptions"
            )
        )
    return out
