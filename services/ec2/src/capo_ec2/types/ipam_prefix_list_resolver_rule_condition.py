"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_prefix_list_resolver_rule_condition_operation
    import capo_ec2.types.ipam_resource_tag
    import capo_ec2.types.string


class IpamPrefixListResolverRuleCondition(TypedDict, closed=True):
    operation: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_rule_condition_operation.IpamPrefixListResolverRuleConditionOperation"
    ]
    """<p>The operation to perform when evaluating this condition. Valid values include <code>equals</code>, <code>not-equals</code>, <code>contains</code>, and <code>not-contains</code>.</p>"""
    ipam_pool_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the IPAM pool to match against. This condition selects CIDRs that belong to the specified IPAM pool.</p>"""
    resource_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services resource to match against. This condition selects CIDRs associated with the specified resource.</p>"""
    resource_owner: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID that owns the resources to match against. This condition selects CIDRs from resources owned by the specified account.</p>"""
    resource_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region where the resources are located. This condition selects CIDRs from resources in the specified Region.</p>"""
    resource_tag: NotRequired["capo_ec2.types.ipam_resource_tag.IpamResourceTag"]
    """<p>A tag key-value pair to match against. This condition selects CIDRs from resources that have the specified tag.</p>"""
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>A CIDR block to match against. This condition selects CIDRs that fall within or match the specified CIDR range.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverRuleCondition,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "operation" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_rule_condition_operation

        capo_ec2.types.ipam_prefix_list_resolver_rule_condition_operation.serialize_ec2_query(
            value["operation"], pairs, f"{key_prefix}Operation"
        )
    if "ipam_pool_id" in value:
        pairs.append((f"{key_prefix}IpamPoolId", str(value["ipam_pool_id"])))
    if "resource_id" in value:
        pairs.append((f"{key_prefix}ResourceId", str(value["resource_id"])))
    if "resource_owner" in value:
        pairs.append((f"{key_prefix}ResourceOwner", str(value["resource_owner"])))
    if "resource_region" in value:
        pairs.append((f"{key_prefix}ResourceRegion", str(value["resource_region"])))
    if "resource_tag" in value:
        import capo_ec2.types.ipam_resource_tag

        capo_ec2.types.ipam_resource_tag.serialize_ec2_query(
            value["resource_tag"], pairs, f"{key_prefix}ResourceTag"
        )
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverRuleCondition:
    out: IpamPrefixListResolverRuleCondition = {}  # type: ignore[typeddict-item]
    child_operation = el.find("operation")
    if child_operation is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_rule_condition_operation

        out["operation"] = (
            capo_ec2.types.ipam_prefix_list_resolver_rule_condition_operation.deserialize_ec2_query(
                child_operation
            )
        )
    child_ipam_pool_id = el.find("ipamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_resource_id = el.find("resourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_owner = el.find("resourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    child_resource_region = el.find("resourceRegion")
    if child_resource_region is not None:
        out["resource_region"] = str(child_resource_region.text or "")
    child_resource_tag = el.find("resourceTag")
    if child_resource_tag is not None:
        import capo_ec2.types.ipam_resource_tag

        out["resource_tag"] = capo_ec2.types.ipam_resource_tag.deserialize_ec2_query(
            child_resource_tag
        )
    child_cidr = el.find("cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    return out
