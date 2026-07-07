"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateFirewallDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.firewall_domain_list_status
    import aws_sdk_route53resolver.types.name
    import aws_sdk_route53resolver.types.resource_id
    import aws_sdk_route53resolver.types.status_message


class UpdateFirewallDomainsResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_route53resolver.types.resource_id.ResourceId"]
    """<p>The ID of the firewall domain list that DNS Firewall just updated.</p>"""
    name: NotRequired["aws_sdk_route53resolver.types.name.Name"]
    """<p>The name of the domain list. </p>"""
    status: NotRequired[
        "aws_sdk_route53resolver.types.firewall_domain_list_status.FirewallDomainListStatus"
    ]
    """<p>Status of the <code>UpdateFirewallDomains</code> request.</p>"""
    status_message: NotRequired[
        "aws_sdk_route53resolver.types.status_message.StatusMessage"
    ]
    """<p>Additional information about the status of the list, if available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFirewallDomainsResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_route53resolver.types.firewall_domain_list_status

        out["Status"] = (
            aws_sdk_route53resolver.types.firewall_domain_list_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFirewallDomainsResponse:
    out: UpdateFirewallDomainsResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_route53resolver.types.firewall_domain_list_status

        out["status"] = (
            aws_sdk_route53resolver.types.firewall_domain_list_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
