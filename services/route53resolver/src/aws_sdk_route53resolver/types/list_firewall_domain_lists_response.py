"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListFirewallDomainListsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_domain_list_metadata_list
    import aws_sdk_route53resolver.types.next_token


class ListFirewallDomainListsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>If objects are still available for retrieval, Resolver returns this token in the response. To retrieve the next batch of objects, provide this token in your next request.</p>"""
    firewall_domain_lists: NotRequired[
        "aws_sdk_route53resolver.types.firewall_domain_list_metadata_list.FirewallDomainListMetadataList"
    ]
    """<p>A list of the domain lists that you have defined. </p> <p>This might be a partial list of the domain lists that you've defined. For information, see <code>MaxResults</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFirewallDomainListsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "firewall_domain_lists" in value:
        import aws_sdk_route53resolver.types.firewall_domain_list_metadata_list

        out["FirewallDomainLists"] = (
            aws_sdk_route53resolver.types.firewall_domain_list_metadata_list.serialize_aws_json_1_1(
                value["firewall_domain_lists"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFirewallDomainListsResponse:
    out: ListFirewallDomainListsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "FirewallDomainLists" in data:
        import aws_sdk_route53resolver.types.firewall_domain_list_metadata_list

        out["firewall_domain_lists"] = (
            aws_sdk_route53resolver.types.firewall_domain_list_metadata_list.deserialize_aws_json_1_1(
                data["FirewallDomainLists"]
            )
        )
    return out
