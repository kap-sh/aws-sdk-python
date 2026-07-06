"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListFirewallRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_rules
    import aws_sdk_route53resolver.types.next_token


class ListFirewallRulesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>If objects are still available for retrieval, Resolver returns this token in the response. To retrieve the next batch of objects, provide this token in your next request.</p>"""
    firewall_rules: NotRequired[
        "aws_sdk_route53resolver.types.firewall_rules.FirewallRules"
    ]
    """<p>A list of the rules that you have defined. </p> <p>This might be a partial list of the firewall rules that you've defined. For information, see <code>MaxResults</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFirewallRulesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "firewall_rules" in value:
        import aws_sdk_route53resolver.types.firewall_rules

        out["FirewallRules"] = (
            aws_sdk_route53resolver.types.firewall_rules.serialize_aws_json_1_1(
                value["firewall_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFirewallRulesResponse:
    out: ListFirewallRulesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "FirewallRules" in data:
        import aws_sdk_route53resolver.types.firewall_rules

        out["firewall_rules"] = (
            aws_sdk_route53resolver.types.firewall_rules.deserialize_aws_json_1_1(
                data["FirewallRules"]
            )
        )
    return out
