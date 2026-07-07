"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetHostedZoneAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class GetHostedZoneAssociationInput(TypedDict, closed=True):
    hosted_zone_association_id: (
        "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    )
    """<p>ID of the private hosted zone association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHostedZoneAssociationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetHostedZoneAssociationInput:
    out: GetHostedZoneAssociationInput = {}  # type: ignore[typeddict-item]
    return out
