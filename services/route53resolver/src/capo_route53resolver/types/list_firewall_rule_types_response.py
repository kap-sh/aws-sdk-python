"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListFirewallRuleTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_rule_type_definitions
    import capo_route53resolver.types.next_token


class ListFirewallRuleTypesResponse(TypedDict, closed=True):
    firewall_rule_types: NotRequired[
        "capo_route53resolver.types.firewall_rule_type_definitions.FirewallRuleTypeDefinitions"
    ]
    """<p>A list of the available rule type definitions.</p>"""
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>If objects are still available for retrieval, Resolver returns this token in the response. To retrieve the next batch of objects, provide this token in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFirewallRuleTypesResponse) -> dict:
    out: dict = {}
    if "firewall_rule_types" in value:
        import capo_route53resolver.types.firewall_rule_type_definitions

        out["FirewallRuleTypes"] = (
            capo_route53resolver.types.firewall_rule_type_definitions.serialize_aws_json_1_1(
                value["firewall_rule_types"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFirewallRuleTypesResponse:
    out: ListFirewallRuleTypesResponse = {}  # type: ignore[typeddict-item]
    if "FirewallRuleTypes" in data:
        import capo_route53resolver.types.firewall_rule_type_definitions

        out["firewall_rule_types"] = (
            capo_route53resolver.types.firewall_rule_type_definitions.deserialize_aws_json_1_1(
                data["FirewallRuleTypes"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
