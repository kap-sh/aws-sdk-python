"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListFirewallDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_domains
    import capo_route53resolver.types.next_token


class ListFirewallDomainsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>If objects are still available for retrieval, Resolver returns this token in the response. To retrieve the next batch of objects, provide this token in your next request.</p>"""
    domains: NotRequired["capo_route53resolver.types.firewall_domains.FirewallDomains"]
    """<p>A list of the domains in the firewall domain list. </p> <p>This might be a partial list of the domains that you've defined in the domain list. For information, see <code>MaxResults</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFirewallDomainsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "domains" in value:
        import capo_route53resolver.types.firewall_domains

        out["Domains"] = (
            capo_route53resolver.types.firewall_domains.serialize_aws_json_1_1(
                value["domains"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFirewallDomainsResponse:
    out: ListFirewallDomainsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Domains" in data:
        import capo_route53resolver.types.firewall_domains

        out["domains"] = (
            capo_route53resolver.types.firewall_domains.deserialize_aws_json_1_1(
                data["Domains"]
            )
        )
    return out
