"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetManagedFirewallDomainListOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name


class GetManagedFirewallDomainListOutput(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>Description of the Managed Domain List.</p>"""
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the Managed Domain List.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>Name of the Managed Domain List.</p>"""
    managed_list_type: "str"
    """<p>Type of the managed category. This is either <code>THREAT</code> or <code>CONTENT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedFirewallDomainListOutput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["managedListType"] = value["managed_list_type"]
    return out


def deserialize_json(data: dict) -> GetManagedFirewallDomainListOutput:
    out: GetManagedFirewallDomainListOutput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetManagedFirewallDomainListOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetManagedFirewallDomainListOutput.name required")
    if "managedListType" in data:
        out["managed_list_type"] = data["managedListType"]
    else:
        raise DeserializationError(
            "GetManagedFirewallDomainListOutput.managed_list_type required"
        )
    return out
