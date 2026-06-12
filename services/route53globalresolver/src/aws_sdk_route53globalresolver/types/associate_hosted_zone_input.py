"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#AssociateHostedZoneInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.hosted_zone_id
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.resource_name


class AssociateHostedZoneInput(TypedDict):
    hosted_zone_id: "aws_sdk_route53globalresolver.types.hosted_zone_id.HostedZoneId"
    """<p>The ID of the Route 53 private hosted zone to associate with the Route 53 Global Resolver resource.</p>"""
    resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>An Amazon Resource Name (ARN) of the Route 53 Global Resolver the private hosted zone will be associated to.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>Name for the private hosted zone association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateHostedZoneInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssociateHostedZoneInput:
    out: AssociateHostedZoneInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("AssociateHostedZoneInput.resource_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssociateHostedZoneInput.name required")
    return out
