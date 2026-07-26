"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteGlobalResolverInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_id


class DeleteGlobalResolverInput(TypedDict, closed=True):
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the Route 53 Global Resolver to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGlobalResolverInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGlobalResolverInput:
    out: DeleteGlobalResolverInput = {}  # type: ignore[typeddict-item]
    return out
