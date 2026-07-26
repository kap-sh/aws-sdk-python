"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#HostedZoneAssociationSummary``."""

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


class HostedZoneAssociationSummary(TypedDict, closed=True):
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the hosted zone association.</p>"""
    resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource associated with the hosted zone.</p>"""
    hosted_zone_id: "capo_route53globalresolver.types.hosted_zone_id.HostedZoneId"
    """<p>The ID of the hosted zone.</p>"""
    hosted_zone_name: "capo_route53globalresolver.types.hosted_zone_name.HostedZoneName"
    """<p>The name of the hosted zone.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the hosted zone association.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the hosted zone association was created.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the hosted zone association was last updated.</p>"""
    status: "capo_route53globalresolver.types.hosted_zone_association_status.HostedZoneAssociationStatus"
    """<p>The current status of the hosted zone association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HostedZoneAssociationSummary) -> dict:
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


def deserialize_json(data: dict) -> HostedZoneAssociationSummary:
    out: HostedZoneAssociationSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("HostedZoneAssociationSummary.id required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("HostedZoneAssociationSummary.resource_arn required")
    if "hostedZoneId" in data:
        out["hosted_zone_id"] = data["hostedZoneId"]
    else:
        raise DeserializationError(
            "HostedZoneAssociationSummary.hosted_zone_id required"
        )
    if "hostedZoneName" in data:
        out["hosted_zone_name"] = data["hostedZoneName"]
    else:
        raise DeserializationError(
            "HostedZoneAssociationSummary.hosted_zone_name required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("HostedZoneAssociationSummary.name required")
    if "createdAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("HostedZoneAssociationSummary.created_at required")
    if "updatedAt" in data:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("HostedZoneAssociationSummary.updated_at required")
    if "status" in data:
        import capo_route53globalresolver.types.hosted_zone_association_status

        out["status"] = (
            capo_route53globalresolver.types.hosted_zone_association_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("HostedZoneAssociationSummary.status required")
    return out
