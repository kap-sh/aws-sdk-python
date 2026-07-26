"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteDNSViewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.resource_id


class DeleteDNSViewInput(TypedDict, closed=True):
    dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the DNS view to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDNSViewInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDNSViewInput:
    out: DeleteDNSViewInput = {}  # type: ignore[typeddict-item]
    return out
