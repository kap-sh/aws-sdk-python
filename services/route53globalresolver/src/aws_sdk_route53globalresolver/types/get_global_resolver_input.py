"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetGlobalResolverInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class GetGlobalResolverInput(TypedDict):
    global_resolver_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Route 53 Global Resolver to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGlobalResolverInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGlobalResolverInput:
    out: GetGlobalResolverInput = {}  # type: ignore[typeddict-item]
    return out
