"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetDNSViewInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class GetDNSViewInput(TypedDict):
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDNSViewInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDNSViewInput:
    out: GetDNSViewInput = {}  # type: ignore[typeddict-item]
    return out
