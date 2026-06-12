"""Generated from Smithy shape ``com.amazonaws.route53resolver#AssociateFirewallRuleGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_rule_group_association


class AssociateFirewallRuleGroupResponse(TypedDict):
    firewall_rule_group_association: NotRequired[
        "aws_sdk_route53resolver.types.firewall_rule_group_association.FirewallRuleGroupAssociation"
    ]
    """<p>The association that you just created. The association has an ID that you can use to identify it in other requests, like update and delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateFirewallRuleGroupResponse) -> dict:
    out: dict = {}
    if "firewall_rule_group_association" in value:
        import aws_sdk_route53resolver.types.firewall_rule_group_association

        out["FirewallRuleGroupAssociation"] = (
            aws_sdk_route53resolver.types.firewall_rule_group_association.serialize_aws_json_1_1(
                value["firewall_rule_group_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateFirewallRuleGroupResponse:
    out: AssociateFirewallRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if "FirewallRuleGroupAssociation" in data:
        import aws_sdk_route53resolver.types.firewall_rule_group_association

        out["firewall_rule_group_association"] = (
            aws_sdk_route53resolver.types.firewall_rule_group_association.deserialize_aws_json_1_1(
                data["FirewallRuleGroupAssociation"]
            )
        )
    return out
