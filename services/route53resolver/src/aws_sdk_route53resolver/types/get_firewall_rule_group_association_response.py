"""Generated from Smithy shape ``com.amazonaws.route53resolver#GetFirewallRuleGroupAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_rule_group_association


class GetFirewallRuleGroupAssociationResponse(TypedDict, closed=True):
    firewall_rule_group_association: NotRequired[
        "aws_sdk_route53resolver.types.firewall_rule_group_association.FirewallRuleGroupAssociation"
    ]
    """<p>The association that you requested. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFirewallRuleGroupAssociationResponse) -> dict:
    out: dict = {}
    if "firewall_rule_group_association" in value:
        import aws_sdk_route53resolver.types.firewall_rule_group_association

        out["FirewallRuleGroupAssociation"] = (
            aws_sdk_route53resolver.types.firewall_rule_group_association.serialize_aws_json_1_1(
                value["firewall_rule_group_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFirewallRuleGroupAssociationResponse:
    out: GetFirewallRuleGroupAssociationResponse = {}  # type: ignore[typeddict-item]
    if "FirewallRuleGroupAssociation" in data:
        import aws_sdk_route53resolver.types.firewall_rule_group_association

        out["firewall_rule_group_association"] = (
            aws_sdk_route53resolver.types.firewall_rule_group_association.deserialize_aws_json_1_1(
                data["FirewallRuleGroupAssociation"]
            )
        )
    return out
