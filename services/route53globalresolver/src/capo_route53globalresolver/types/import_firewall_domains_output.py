"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ImportFirewallDomainsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class ImportFirewallDomainsOutput(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the DNS Firewall domain list that you imported the domain list to.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>Name of the DNS Firewall domain list.</p>"""
    status: "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>Operational status of the DNS Firewall domain list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportFirewallDomainsOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_route53globalresolver.types.cr_resource_status

    out["status"] = capo_route53globalresolver.types.cr_resource_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> ImportFirewallDomainsOutput:
    out: ImportFirewallDomainsOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ImportFirewallDomainsOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ImportFirewallDomainsOutput.name required")
    if "status" in data:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ImportFirewallDomainsOutput.status required")
    return out
