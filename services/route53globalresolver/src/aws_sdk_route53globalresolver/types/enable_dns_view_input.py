"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#EnableDNSViewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class EnableDNSViewInput(TypedDict, closed=True):
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the DNS view to enable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableDNSViewInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EnableDNSViewInput:
    out: EnableDNSViewInput = {}  # type: ignore[typeddict-item]
    return out
