"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ListManagedFirewallDomainListsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.managed_firewall_domain_lists


class ListManagedFirewallDomainListsOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>A pagination token used for large sets of results that can't be returned in a single response. Provide this token in the next call to get the results not returned in this call.</p>"""
    managed_firewall_domain_lists: "aws_sdk_route53globalresolver.types.managed_firewall_domain_lists.ManagedFirewallDomainLists"
    """<p>List of the Managed Domain Lists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedFirewallDomainListsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_route53globalresolver.types.managed_firewall_domain_lists

    out["managedFirewallDomainLists"] = (
        aws_sdk_route53globalresolver.types.managed_firewall_domain_lists.serialize_json(
            value["managed_firewall_domain_lists"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListManagedFirewallDomainListsOutput:
    out: ListManagedFirewallDomainListsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "managedFirewallDomainLists" in data:
        import aws_sdk_route53globalresolver.types.managed_firewall_domain_lists

        out["managed_firewall_domain_lists"] = (
            aws_sdk_route53globalresolver.types.managed_firewall_domain_lists.deserialize_json(
                data["managedFirewallDomainLists"]
            )
        )
    else:
        raise DeserializationError(
            "ListManagedFirewallDomainListsOutput.managed_firewall_domain_lists required"
        )
    return out
