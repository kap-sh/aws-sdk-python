"""Generated from Smithy shape ``com.amazonaws.route53resolver#ImportFirewallDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_domain_list_status
    import capo_route53resolver.types.name
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.status_message


class ImportFirewallDomainsResponse(TypedDict, closed=True):
    id: NotRequired["capo_route53resolver.types.resource_id.ResourceId"]
    """<p>The Id of the firewall domain list that DNS Firewall just updated.</p>"""
    name: NotRequired["capo_route53resolver.types.name.Name"]
    """<p>The name of the domain list. </p>"""
    status: NotRequired[
        "capo_route53resolver.types.firewall_domain_list_status.FirewallDomainListStatus"
    ]
    """<p>Status of the import request.</p>"""
    status_message: NotRequired[
        "capo_route53resolver.types.status_message.StatusMessage"
    ]
    """<p>Additional information about the status of the list, if available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportFirewallDomainsResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_route53resolver.types.firewall_domain_list_status

        out["Status"] = (
            capo_route53resolver.types.firewall_domain_list_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportFirewallDomainsResponse:
    out: ImportFirewallDomainsResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import capo_route53resolver.types.firewall_domain_list_status

        out["status"] = (
            capo_route53resolver.types.firewall_domain_list_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
