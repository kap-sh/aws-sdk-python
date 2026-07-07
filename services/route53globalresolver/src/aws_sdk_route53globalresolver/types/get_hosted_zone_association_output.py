"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetHostedZoneAssociationOutput``."""

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


class GetHostedZoneAssociationOutput(TypedDict, closed=True):
    id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>ID of the private hosted zone association.</p>"""
    resource_arn: "aws_sdk_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>Amazon Resource Name (ARN) of the DNS view the private hosted zone is associated to.</p>"""
    hosted_zone_id: "aws_sdk_route53globalresolver.types.hosted_zone_id.HostedZoneId"
    """<p>ID of the hosted zone associated to the DNS view.</p>"""
    hosted_zone_name: (
        "aws_sdk_route53globalresolver.types.hosted_zone_name.HostedZoneName"
    )
    """<p>Name of the domain associated with the private hosted zone.</p>"""
    name: "aws_sdk_route53globalresolver.types.resource_name.ResourceName"
    """<p>Name of the private hosted zone association.</p>"""
    created_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The time and date the private hosted zone association was created.</p>"""
    updated_at: (
        "aws_sdk_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    )
    """<p>The time and date the private hosted zone association was updated.</p>"""
    status: "aws_sdk_route53globalresolver.types.hosted_zone_association_status.HostedZoneAssociationStatus"
    """<p>The operational status of the private hosted zone association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHostedZoneAssociationOutput) -> dict:
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


def deserialize_json(data: dict) -> GetHostedZoneAssociationOutput:
    out: GetHostedZoneAssociationOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetHostedZoneAssociationOutput.id required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "GetHostedZoneAssociationOutput.resource_arn required"
        )
    if "hostedZoneId" in data:
        out["hosted_zone_id"] = data["hostedZoneId"]
    else:
        raise DeserializationError(
            "GetHostedZoneAssociationOutput.hosted_zone_id required"
        )
    if "hostedZoneName" in data:
        out["hosted_zone_name"] = data["hostedZoneName"]
    else:
        raise DeserializationError(
            "GetHostedZoneAssociationOutput.hosted_zone_name required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetHostedZoneAssociationOutput.name required")
    if "createdAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetHostedZoneAssociationOutput.created_at required")
    if "updatedAt" in data:
        import aws_sdk_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            aws_sdk_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetHostedZoneAssociationOutput.updated_at required")
    if "status" in data:
        import aws_sdk_route53globalresolver.types.hosted_zone_association_status

        out["status"] = (
            aws_sdk_route53globalresolver.types.hosted_zone_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetHostedZoneAssociationOutput.status required")
    return out
