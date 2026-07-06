"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DisassociateHostedZoneOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.hosted_zone_association_status
    import aws_sdk_route53globalresolver.types.hosted_zone_id
    import aws_sdk_route53globalresolver.types.hosted_zone_name
    import aws_sdk_route53globalresolver.types.iso8601_time_string
    import aws_sdk_route53globalresolver.types.resource_arn
    import aws_sdk_route53globalresolver.types.resource_id
    import aws_sdk_route53globalresolver.types.resource_name


class DisassociateHostedZoneOutput(TypedDict, closed=True):
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the disassociation.</p>"""
    resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Route 53 Global Resolver resource that the hosted zone was disassociated from.</p>"""
    hosted_zone_id: "aws_sdk_route53globalresolver.types.hosted_zone_id.HostedZoneId"
    """<p>The ID of the Route 53 private hosted zone that was disassociated.</p>"""
    hosted_zone_name: (
        "aws_sdk_route53globalresolver.types.hosted_zone_name.HostedZoneName"
    )
    """<p>The name of the Route 53 private hosted zone that was disassociated.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the association that was removed.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the association was originally created.</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The date and time when the association was last updated before disassociation.</p>"""
    status: "aws_sdk_route53globalresolver.types.hosted_zone_association_status.HostedZoneAssociationStatus"
    """<p>The final status of the disassociation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateHostedZoneOutput) -> dict:
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


def deserialize_json(data: dict) -> DisassociateHostedZoneOutput:
    out: DisassociateHostedZoneOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DisassociateHostedZoneOutput.id required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("DisassociateHostedZoneOutput.resource_arn required")
    if "hostedZoneId" in data:
        out["hosted_zone_id"] = data["hostedZoneId"]
    else:
        raise DeserializationError(
            "DisassociateHostedZoneOutput.hosted_zone_id required"
        )
    if "hostedZoneName" in data:
        out["hosted_zone_name"] = data["hostedZoneName"]
    else:
        raise DeserializationError(
            "DisassociateHostedZoneOutput.hosted_zone_name required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DisassociateHostedZoneOutput.name required")
    if "createdAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DisassociateHostedZoneOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DisassociateHostedZoneOutput.updated_at required")
    if "status" in data:
        import aws_sdk_route53globalresolver.types.hosted_zone_association_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.hosted_zone_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DisassociateHostedZoneOutput.status required")
    return out
