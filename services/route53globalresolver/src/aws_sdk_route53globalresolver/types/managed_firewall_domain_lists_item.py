"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#ManagedFirewallDomainListsItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name


class ManagedFirewallDomainListsItem(TypedDict):
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>A description of the managed firewall domain list.</p>"""
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the managed firewall domain list.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the managed firewall domain list.</p>"""
    managed_list_type: "str"
    """<p>The type of the managed firewall domain list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedFirewallDomainListsItem) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["managedListType"] = value["managed_list_type"]
    return out


def deserialize_json(data: dict) -> ManagedFirewallDomainListsItem:
    out: ManagedFirewallDomainListsItem = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ManagedFirewallDomainListsItem.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ManagedFirewallDomainListsItem.name required")
    if "managedListType" in data:
        out["managed_list_type"] = data["managedListType"]
    else:
        raise DeserializationError(
            "ManagedFirewallDomainListsItem.managed_list_type required"
        )
    return out
