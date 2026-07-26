"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_policy_allocation_rule_list
    import capo_ec2.types.ipam_policy_id
    import capo_ec2.types.ipam_policy_resource_type
    import capo_ec2.types.string


class IpamPolicyDocument(TypedDict, closed=True):
    ipam_policy_id: NotRequired["capo_ec2.types.ipam_policy_id.IpamPolicyId"]
    """<p>The ID of the IPAM policy.</p>"""
    locale: NotRequired["capo_ec2.types.string.String"]
    """<p>The locale of the IPAM policy document.</p>"""
    resource_type: NotRequired[
        "capo_ec2.types.ipam_policy_resource_type.IpamPolicyResourceType"
    ]
    """<p>The resource type of the IPAM policy document.</p> <p>The Amazon Web Services service or resource type that can use IP addresses through IPAM policies. Supported services and resource types include:</p> <ul> <li> <p>Elastic IP addresses</p> </li> </ul>"""
    allocation_rules: NotRequired[
        "capo_ec2.types.ipam_policy_allocation_rule_list.IpamPolicyAllocationRuleList"
    ]
    """<p>The allocation rules in the IPAM policy document.</p> <p>Allocation rules are optional configurations within an IPAM policy that map Amazon Web Services resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPolicyDocument, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_policy_id" in value:
        pairs.append((f"{prefix}.IpamPolicyId", str(value["ipam_policy_id"])))
    if "locale" in value:
        pairs.append((f"{prefix}.Locale", str(value["locale"])))
    if "resource_type" in value:
        import capo_ec2.types.ipam_policy_resource_type

        capo_ec2.types.ipam_policy_resource_type.serialize_ec2_query(
            value["resource_type"], pairs, f"{prefix}.ResourceType"
        )
    if "allocation_rules" in value:
        import capo_ec2.types.ipam_policy_allocation_rule_list

        capo_ec2.types.ipam_policy_allocation_rule_list.serialize_ec2_query(
            value["allocation_rules"], pairs, f"{prefix}.AllocationRuleSet"
        )


def deserialize_ec2_query(el: Element) -> IpamPolicyDocument:
    out: IpamPolicyDocument = {}  # type: ignore[typeddict-item]
    child_ipam_policy_id = el.find("IpamPolicyId")
    if child_ipam_policy_id is not None:
        out["ipam_policy_id"] = str(child_ipam_policy_id.text or "")
    child_locale = el.find("Locale")
    if child_locale is not None:
        out["locale"] = str(child_locale.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        import capo_ec2.types.ipam_policy_resource_type

        out["resource_type"] = (
            capo_ec2.types.ipam_policy_resource_type.deserialize_ec2_query(
                child_resource_type
            )
        )
    if el.find("AllocationRuleSet") is not None:
        import capo_ec2.types.ipam_policy_allocation_rule_list

        out["allocation_rules"] = (
            capo_ec2.types.ipam_policy_allocation_rule_list.deserialize_ec2_query(
                el, "AllocationRuleSet"
            )
        )
    return out
