"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListFirewallDomainListsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.firewall_domain_lists


class ListFirewallDomainListsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    firewall_domain_lists: (
        "aws_sdk_route53globalresolver.types.firewall_domain_lists.FirewallDomainLists"
    )
    """<p>List of the DNS Firewall domain lists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFirewallDomainListsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_route53globalresolver.types.firewall_domain_lists

    out["firewallDomainLists"] = (
        aws_sdk_route53globalresolver.types.firewall_domain_lists.serialize_json(
            value["firewall_domain_lists"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListFirewallDomainListsOutput:
    out: ListFirewallDomainListsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "firewallDomainLists" in data:
        import aws_sdk_route53globalresolver.types.firewall_domain_lists

        out["firewall_domain_lists"] = (
            aws_sdk_route53globalresolver.types.firewall_domain_lists.deserialize_json(
                data["firewallDomainLists"]
            )
        )
    else:
        raise DeserializationError(
            "ListFirewallDomainListsOutput.firewall_domain_lists required"
        )
    return out
