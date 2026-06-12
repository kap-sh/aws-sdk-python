"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateHostedZoneAssociationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name


class UpdateHostedZoneAssociationInput(TypedDict):
    hosted_zone_association_id: (
        "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    )
    """<p>The ID of the private hosted zone association.</p>"""
    name: NotRequired["aws_sdk_route53globalresolver.types.resource_name.ResourceName"]
    """<p>The name you want to update the hosted zone association to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateHostedZoneAssociationInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateHostedZoneAssociationInput:
    out: UpdateHostedZoneAssociationInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
