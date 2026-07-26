"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DisassociateHostedZoneInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.hosted_zone_id
    import capo_route53globalresolver.types.resource_arn


class DisassociateHostedZoneInput(TypedDict, closed=True):
    hosted_zone_id: "capo_route53globalresolver.types.hosted_zone_id.HostedZoneId"
    """<p>The ID of the Route 53 private hosted zone to disassociate.</p>"""
    resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Route 53 Global Resolver resource to disassociate the hosted zone from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateHostedZoneInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateHostedZoneInput:
    out: DisassociateHostedZoneInput = {}  # type: ignore[typeddict-item]
    return out
