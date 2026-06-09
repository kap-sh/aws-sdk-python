"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_request_set
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_type
    import aws_sdk_ec2.types.ipam_resource_type
    import aws_sdk_ec2.types.ipam_scope_id
    import aws_sdk_ec2.types.string


class IpamPrefixListResolverRuleRequest(TypedDict):
    rule_type: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_type.IpamPrefixListResolverRuleType"
    ]
    """<p>The type of CIDR selection rule. Valid values include <code>include</code> for selecting CIDRs that match the conditions, and <code>exclude</code> for excluding CIDRs that match the conditions.</p>"""
    static_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A fixed list of CIDRs that do not change (like a manual list replicated across Regions).</p>"""
    ipam_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the IPAM scope from which to select CIDRs. This determines whether to select from public or private IP address space.</p>"""
    resource_type: NotRequired["aws_sdk_ec2.types.ipam_resource_type.IpamResourceType"]
    """<p>For rules of type <code>ipam-resource-cidr</code>, this is the resource type.</p>"""
    conditions: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_request_set.IpamPrefixListResolverRuleConditionRequestSet"
    ]
    """<p>The conditions that determine which CIDRs are selected by this rule. Conditions specify criteria such as resource type, tags, account IDs, and Regions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverRuleRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "rule_type" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_type

        aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_type.serialize_ec2_query(
            value["rule_type"], pairs, f"{prefix}.RuleType"
        )
    if "static_cidr" in value:
        pairs.append((f"{prefix}.StaticCidr", str(value["static_cidr"])))
    if "ipam_scope_id" in value:
        pairs.append((f"{prefix}.IpamScopeId", str(value["ipam_scope_id"])))
    if "resource_type" in value:
        import aws_sdk_ec2.types.ipam_resource_type

        aws_sdk_ec2.types.ipam_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "conditions" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_request_set

        aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_request_set.serialize_ec2_query(
            value["conditions"], pairs, f"{prefix}.Conditions"
        )


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverRuleRequest:
    out: IpamPrefixListResolverRuleRequest = {}  # type: ignore[typeddict-item]
    child_rule_type = el.find("RuleType")
    if child_rule_type is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_type

        out["rule_type"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_type.deserialize_ec2_query(
                child_rule_type
            )
        )
    child_static_cidr = el.find("StaticCidr")
    if child_static_cidr is not None:
        out["static_cidr"] = str(child_static_cidr.text or "")
    child_ipam_scope_id = el.find("IpamScopeId")
    if child_ipam_scope_id is not None:
        out["ipam_scope_id"] = str(child_ipam_scope_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import aws_sdk_ec2.types.ipam_resource_type

        out["resource_type"] = (
            aws_sdk_ec2.types.ipam_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    if el.find("Conditions") is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_request_set

        out["conditions"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_request_set.deserialize_ec2_query(
                el, "Conditions"
            )
        )
    return out
