"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateFirewallDomainListInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.client_token
    import aws_sdk_route53globalresolver.types.resource_description
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name
    import aws_sdk_route53globalresolver.types.tags


class CreateFirewallDomainListInput(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same <code>clientToken</code> has the same result every time.</p>"""
    global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Route 53 Global Resolver that the domain list will be associated with.</p>"""
    description: NotRequired[
        "aws_sdk_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>An optional description for the firewall domain list.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>A descriptive name for the firewall domain list.</p>"""
    tags: NotRequired["aws_sdk_route53globalresolver.types.tags.Tags"]
    """<p>An array of user-defined keys and optional values. These tags can be used for categorization and organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFirewallDomainListInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_route53globalresolver.types.tags

        out["tags"] = aws_sdk_route53globalresolver.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateFirewallDomainListInput:
    out: CreateFirewallDomainListInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFirewallDomainListInput.name required")
    if "tags" in data:
        import aws_sdk_route53globalresolver.types.tags

        out["tags"] = aws_sdk_route53globalresolver.types.tags.deserialize_json(
            data["tags"]
        )
    return out
