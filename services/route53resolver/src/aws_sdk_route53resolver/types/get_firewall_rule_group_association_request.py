"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetFirewallRuleGroupAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.resource_id


class GetFirewallRuleGroupAssociationRequest(TypedDict):
    firewall_rule_group_association_id: (
        "aws_sdk_route53resolver.types.resource_id.ResourceId"
    )
    """<p>The identifier of the <a>FirewallRuleGroupAssociation</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFirewallRuleGroupAssociationRequest) -> dict:
    out: dict = {}
    out["FirewallRuleGroupAssociationId"] = value["firewall_rule_group_association_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFirewallRuleGroupAssociationRequest:
    out: GetFirewallRuleGroupAssociationRequest = {}  # type: ignore[typeddict-item]
    if "FirewallRuleGroupAssociationId" in data:
        out["firewall_rule_group_association_id"] = data[
            "FirewallRuleGroupAssociationId"
        ]
    else:
        raise DeserializationError(
            "GetFirewallRuleGroupAssociationRequest.firewall_rule_group_association_id required"
        )
    return out
