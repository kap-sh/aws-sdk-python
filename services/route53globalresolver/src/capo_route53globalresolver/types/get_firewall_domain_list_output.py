"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetFirewallDomainListOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class GetFirewallDomainListOutput(TypedDict, closed=True):
    arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>Amazon Resource Name (ARN) of the domain list.</p>"""
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the Global Resolver that the domain list is associated to.</p>"""
    client_token: NotRequired[
        "capo_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The time and date the domain list was created.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the domain list.</p>"""
    domain_count: "int"
    """<p>Number of domains in the domain list.</p>"""
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the domain list.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>Name of the domain list.</p>"""
    status: "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>Operational status of the domain list.</p>"""
    status_message: NotRequired["str"]
    """<p>Additional information about the status of the domain list.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time the domain list was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFirewallDomainListOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["globalResolverId"] = value["global_resolver_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    out["domainCount"] = value["domain_count"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_route53globalresolver.types.cr_resource_status

    out["status"] = capo_route53globalresolver.types.cr_resource_status.serialize_json(
        value["status"]
    )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetFirewallDomainListOutput:
    out: GetFirewallDomainListOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetFirewallDomainListOutput.arn required")
    if "globalResolverId" in data:
        out["global_resolver_id"] = data["globalResolverId"]
    else:
        raise DeserializationError(
            "GetFirewallDomainListOutput.global_resolver_id required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "createdAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetFirewallDomainListOutput.created_at required")
    if "description" in data:
        out["description"] = data["description"]
    if "domainCount" in data:
        out["domain_count"] = data["domainCount"]
    else:
        raise DeserializationError("GetFirewallDomainListOutput.domain_count required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetFirewallDomainListOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetFirewallDomainListOutput.name required")
    if "status" in data:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetFirewallDomainListOutput.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "updatedAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetFirewallDomainListOutput.updated_at required")
    return out
