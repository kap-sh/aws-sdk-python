"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverRuleConditionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_operation
    import aws_sdk_ec2.types.request_ipam_resource_tag
    import aws_sdk_ec2.types.string


class IpamPrefixListResolverRuleConditionRequest(TypedDict, closed=True):
    operation: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_operation.IpamPrefixListResolverRuleConditionOperation"
    ]
    """<p>The operation to perform when evaluating this condition.</p>"""
    ipam_pool_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the IPAM pool to match against. This condition selects CIDRs that belong to the specified IPAM pool.</p>"""
    resource_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services resource to match against. This condition selects CIDRs associated with the specified resource.</p>"""
    resource_owner: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID that owns the resources to match against. This condition selects CIDRs from resources owned by the specified account.</p>"""
    resource_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region where the resources are located. This condition selects CIDRs from resources in the specified Region.</p>"""
    resource_tag: NotRequired[
        "aws_sdk_ec2.types.request_ipam_resource_tag.RequestIpamResourceTag"
    ]
    """<p>A tag key-value pair to match against. This condition selects CIDRs from resources that have the specified tag.</p>"""
    cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A CIDR block to match against. This condition selects CIDRs that fall within or match the specified CIDR range.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverRuleConditionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "operation" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_operation

        aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_operation.serialize_ec2_query(
            value["operation"], pairs, f"{prefix}.Operation"
        )
    if "ipam_pool_id" in value:
        pairs.append((f"{prefix}.IpamPoolId", str(value["ipam_pool_id"])))
    if "resource_id" in value:
        pairs.append((f"{prefix}.ResourceId", str(value["resource_id"])))
    if "resource_owner" in value:
        pairs.append((f"{prefix}.ResourceOwner", str(value["resource_owner"])))
    if "resource_region" in value:
        pairs.append((f"{prefix}.ResourceRegion", str(value["resource_region"])))
    if "resource_tag" in value:
        import aws_sdk_ec2.types.request_ipam_resource_tag

        aws_sdk_ec2.types.request_ipam_resource_tag.serialize_ec2_query(
            value["resource_tag"], pairs, f"{prefix}.ResourceTag"
        )
    if "cidr" in value:
        pairs.append((f"{prefix}.Cidr", str(value["cidr"])))


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverRuleConditionRequest:
    out: IpamPrefixListResolverRuleConditionRequest = {}  # type: ignore[typeddict-item]
    child_operation = el.find("Operation")
    if child_operation is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_operation

        out["operation"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver_rule_condition_operation.deserialize_ec2_query(
                child_operation
            )
        )
    child_ipam_pool_id = el.find("IpamPoolId")
    if child_ipam_pool_id is not None:
        out["ipam_pool_id"] = str(child_ipam_pool_id.text or "")
    child_resource_id = el.find("ResourceId")
    if child_resource_id is not None:
        out["resource_id"] = str(child_resource_id.text or "")
    child_resource_owner = el.find("ResourceOwner")
    if child_resource_owner is not None:
        out["resource_owner"] = str(child_resource_owner.text or "")
    child_resource_region = el.find("ResourceRegion")
    if child_resource_region is not None:
        out["resource_region"] = str(child_resource_region.text or "")
    child_resource_tag = el.find("ResourceTag")
    if child_resource_tag is not None:
        import aws_sdk_ec2.types.request_ipam_resource_tag

        out["resource_tag"] = (
            aws_sdk_ec2.types.request_ipam_resource_tag.deserialize_ec2_query(
                child_resource_tag
            )
        )
    child_cidr = el.find("Cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    return out
