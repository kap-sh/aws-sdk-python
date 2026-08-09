"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_condition_set
    import capo_ec2.types.ipam_prefix_list_resolver_rule_type
    import capo_ec2.types.ipam_resource_type
    import capo_ec2.types.ipam_scope_id
    import capo_ec2.types.string


class IpamPrefixListResolverRule(TypedDict, closed=True):
    rule_type: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_rule_type.IpamPrefixListResolverRuleType"
    ]
    """<p>The type of CIDR selection rule. Valid values include <code>include</code> for selecting CIDRs that match the conditions, and <code>exclude</code> for excluding CIDRs that match the conditions.</p>"""
    static_cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>A fixed list of CIDRs that do not change (like a manual list replicated across Regions).</p>"""
    ipam_scope_id: NotRequired["capo_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the IPAM scope from which to select CIDRs. This determines whether to select from public or private IP address space.</p>"""
    resource_type: NotRequired["capo_ec2.types.ipam_resource_type.IpamResourceType"]
    """<p>For rules of type <code>ipam-resource-cidr</code>, this is the resource type.</p>"""
    conditions: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_rule_condition_set.IpamPrefixListResolverRuleConditionSet"
    ]
    """<p>The conditions that determine which CIDRs are selected by this rule. Conditions specify criteria such as resource type, tags, account IDs, and Regions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverRule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "rule_type" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_rule_type

        capo_ec2.types.ipam_prefix_list_resolver_rule_type.serialize_ec2_query(
            value["rule_type"], pairs, f"{key_prefix}RuleType"
        )
    if "static_cidr" in value:
        pairs.append((f"{key_prefix}StaticCidr", str(value["static_cidr"])))
    if "ipam_scope_id" in value:
        pairs.append((f"{key_prefix}IpamScopeId", str(value["ipam_scope_id"])))
    if "resource_type" in value:
        import capo_ec2.types.ipam_resource_type

        capo_ec2.types.ipam_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{key_prefix}ResourceType"
        )
    if "conditions" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_rule_condition_set

        capo_ec2.types.ipam_prefix_list_resolver_rule_condition_set.serialize_ec2_query(
            value["conditions"], pairs, f"{key_prefix}ConditionSet"
        )


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverRule:
    out: IpamPrefixListResolverRule = {}  # type: ignore[typeddict-item]
    child_rule_type = el.find("ruleType")
    if child_rule_type is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_rule_type

        out["rule_type"] = (
            capo_ec2.types.ipam_prefix_list_resolver_rule_type.deserialize_ec2_query(
                child_rule_type
            )
        )
    child_static_cidr = el.find("staticCidr")
    if child_static_cidr is not None:
        out["static_cidr"] = str(child_static_cidr.text or "")
    child_ipam_scope_id = el.find("ipamScopeId")
    if child_ipam_scope_id is not None:
        out["ipam_scope_id"] = str(child_ipam_scope_id.text or "")
    child_resource_type = el.find("resourceType")
    if child_resource_type is not None:
        import capo_ec2.types.ipam_resource_type

        out["resource_type"] = capo_ec2.types.ipam_resource_type.deserialize_ec2_query(
            child_resource_type
        )
    child_conditions = el.find("conditionSet")
    if child_conditions is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_rule_condition_set

        out["conditions"] = (
            capo_ec2.types.ipam_prefix_list_resolver_rule_condition_set.deserialize_ec2_query(
                child_conditions
            )
        )
    return out
