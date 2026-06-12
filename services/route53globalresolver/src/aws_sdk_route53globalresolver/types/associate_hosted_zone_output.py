"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#AssociateHostedZoneOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.hosted_zone_association_status
    import aws_sdk_route53globalresolver.types.hosted_zone_id
    import aws_sdk_route53globalresolver.types.hosted_zone_name
    import aws_sdk_route53globalresolver.types.iso8601_time_string
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name


class AssociateHostedZoneOutput(TypedDict):
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the association.</p>"""
    resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>An Amazon Resource Name (ARN) of the Route 53 Global Resolver the private hosted zone is associated to.</p>"""
    hosted_zone_id: "aws_sdk_route53globalresolver.types.hosted_zone_id.HostedZoneId"
    """<p>ID of the private hosted zone.</p>"""
    hosted_zone_name: (
        "aws_sdk_route53globalresolver.types.hosted_zone_name.HostedZoneName"
    )
    """<p>Name of the hosted zone (also the domain associated with the hosted zone).</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>Name for the private hosted zone association.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time the private hosted zone association was created.</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time the private hosted zone association was modified.</p>"""
    status: "aws_sdk_route53globalresolver.types.hosted_zone_association_status.HostedZoneAssociationStatus"
    """<p>Aggregate status for all the Amazon Web Services Regions in which the Route 53 Global Resolver exists.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateHostedZoneOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["resourceArn"] = value["resource_arn"]
    out["hostedZoneId"] = value["hosted_zone_id"]
    out["hostedZoneName"] = value["hosted_zone_name"]
    out["name"] = value["name"]
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        aws_sdk_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    import aws_sdk_route53globalresolver.types.hosted_zone_association_status

    out["status"] = (
        aws_sdk_route53globalresolver.types.hosted_zone_association_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssociateHostedZoneOutput:
    out: AssociateHostedZoneOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AssociateHostedZoneOutput.id required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("AssociateHostedZoneOutput.resource_arn required")
    if "hostedZoneId" in data:
        out["hosted_zone_id"] = data["hostedZoneId"]
    else:
        raise DeserializationError("AssociateHostedZoneOutput.hosted_zone_id required")
    if "hostedZoneName" in data:
        out["hosted_zone_name"] = data["hostedZoneName"]
    else:
        raise DeserializationError(
            "AssociateHostedZoneOutput.hosted_zone_name required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssociateHostedZoneOutput.name required")
    if "createdAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("AssociateHostedZoneOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("AssociateHostedZoneOutput.updated_at required")
    if "status" in data:
        import aws_sdk_route53globalresolver.types.hosted_zone_association_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.hosted_zone_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("AssociateHostedZoneOutput.status required")
    return out
