"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DisableDNSViewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class DisableDNSViewInput(TypedDict, closed=True):
    dns_view_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the DNS view to disable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableDNSViewInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableDNSViewInput:
    out: DisableDNSViewInput = {}  # type: ignore[typeddict-item]
    return out
