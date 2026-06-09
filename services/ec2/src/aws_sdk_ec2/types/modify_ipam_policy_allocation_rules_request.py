"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpamPolicyAllocationRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_policy_allocation_rule_list_request
    import aws_sdk_ec2.types.ipam_policy_id
    import aws_sdk_ec2.types.ipam_policy_resource_type
    import aws_sdk_ec2.types.string


class ModifyIpamPolicyAllocationRulesRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_policy_id: NotRequired["aws_sdk_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy whose allocation rules you want to modify.</p>"""
    locale: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The locale for which to modify the allocation rules.</p>"""
    resource_type: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_resource_type.IpamPolicyResourceType"
    ]
    """<p>The resource type for which to modify the allocation rules.</p> <p>The Amazon Web Services service or resource type that can use IP addresses through IPAM policies. Supported services and resource types include:</p> <ul> <li> <p>Elastic IP addresses</p> </li> </ul>"""
    allocation_rules: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_allocation_rule_list_request.IpamPolicyAllocationRuleListRequest"
    ]
    """<p>The new allocation rules to apply to the IPAM policy.</p> <p>Allocation rules are optional configurations within an IPAM policy that map Amazon Web Services resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyIpamPolicyAllocationRulesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_policy_id" in value:
        pairs.append((f"{prefix}.IpamPolicyId", str(value["ipam_policy_id"])))
    if "locale" in value:
        pairs.append((f"{prefix}.Locale", str(value["locale"])))
    if "resource_type" in value:
        import aws_sdk_ec2.types.ipam_policy_resource_type

        aws_sdk_ec2.types.ipam_policy_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "allocation_rules" in value:
        import aws_sdk_ec2.types.ipam_policy_allocation_rule_list_request

        aws_sdk_ec2.types.ipam_policy_allocation_rule_list_request.serialize_ec2_query(
            value["allocation_rules"], pairs, f"{prefix}.AllocationRules"
        )


def deserialize_ec2_query(el: Element) -> ModifyIpamPolicyAllocationRulesRequest:
    out: ModifyIpamPolicyAllocationRulesRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_policy_id = el.find("IpamPolicyId")
    if child_ipam_policy_id is not None:
        out["ipam_policy_id"] = str(child_ipam_policy_id.text or "")
    child_locale = el.find("Locale")
    if child_locale is not None:
        out["locale"] = str(child_locale.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.ipam_policy_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.ipam_policy_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    if el.find("AllocationRules") is not None:
        import aws_sdk_ec2.types.ipam_policy_allocation_rule_list_request

        out["allocation_rules"] = (
            aws_sdk_ec2.types.ipam_policy_allocation_rule_list_request.deserialize_ec2_query(
                el, "AllocationRules"
            )
        )
    return out
