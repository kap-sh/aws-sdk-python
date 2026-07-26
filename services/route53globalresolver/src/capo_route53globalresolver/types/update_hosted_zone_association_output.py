"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateHostedZoneAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.hosted_zone_association_status
    import capo_route53globalresolver.types.hosted_zone_id
    import capo_route53globalresolver.types.hosted_zone_name
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class UpdateHostedZoneAssociationOutput(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the private hosted zone association.</p>"""
    resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the private hosted zone association.</p>"""
    hosted_zone_id: "capo_route53globalresolver.types.hosted_zone_id.HostedZoneId"
    """<p>The ID of the private hosted zone.</p>"""
    hosted_zone_name: "capo_route53globalresolver.types.hosted_zone_name.HostedZoneName"
    """<p>The name of the domain associated with the private hosted zone.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the private hosted zone association.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The time and date the private hosted zone association was created.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The time and date the private hosted zone association was updated.</p>"""
    status: "capo_route53globalresolver.types.hosted_zone_association_status.HostedZoneAssociationStatus"
    """<p>The operational status of the private hosted zone association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateHostedZoneAssociationOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["resourceArn"] = value["resource_arn"]
    out["hostedZoneId"] = value["hosted_zone_id"]
    out["hostedZoneName"] = value["hosted_zone_name"]
    out["name"] = value["name"]
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    import capo_route53globalresolver.types.hosted_zone_association_status

    out["status"] = (
        capo_route53globalresolver.types.hosted_zone_association_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateHostedZoneAssociationOutput:
    out: UpdateHostedZoneAssociationOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateHostedZoneAssociationOutput.id required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "UpdateHostedZoneAssociationOutput.resource_arn required"
        )
    if "hostedZoneId" in data:
        out["hosted_zone_id"] = data["hostedZoneId"]
    else:
        raise DeserializationError(
            "UpdateHostedZoneAssociationOutput.hosted_zone_id required"
        )
    if "hostedZoneName" in data:
        out["hosted_zone_name"] = data["hostedZoneName"]
    else:
        raise DeserializationError(
            "UpdateHostedZoneAssociationOutput.hosted_zone_name required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateHostedZoneAssociationOutput.name required")
    if "createdAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateHostedZoneAssociationOutput.created_at required"
        )
    if "updatedAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateHostedZoneAssociationOutput.updated_at required"
        )
    if "status" in data:
        import capo_route53globalresolver.types.hosted_zone_association_status

        out["status"] = (
            capo_route53globalresolver.types.hosted_zone_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateHostedZoneAssociationOutput.status required")
    return out
