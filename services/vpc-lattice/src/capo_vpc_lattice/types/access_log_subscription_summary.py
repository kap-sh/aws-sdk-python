"""Generated from Smithy shape ``com.amazonaws.vpclattice#AccessLogSubscriptionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.access_log_destination_arn
    import capo_vpc_lattice.types.access_log_subscription_arn
    import capo_vpc_lattice.types.access_log_subscription_id
    import capo_vpc_lattice.types.resource_arn
    import capo_vpc_lattice.types.resource_id
    import capo_vpc_lattice.types.service_network_log_type
    import capo_vpc_lattice.types.timestamp


class AccessLogSubscriptionSummary(TypedDict, closed=True):
    id: "capo_vpc_lattice.types.access_log_subscription_id.AccessLogSubscriptionId"
    """<p>The ID of the access log subscription.</p>"""
    arn: "capo_vpc_lattice.types.access_log_subscription_arn.AccessLogSubscriptionArn"
    """<p>The Amazon Resource Name (ARN) of the access log subscription</p>"""
    resource_id: "capo_vpc_lattice.types.resource_id.ResourceId"
    """<p>The ID of the service or service network.</p>"""
    resource_arn: "capo_vpc_lattice.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the service or service network.</p>"""
    destination_arn: (
        "capo_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the destination.</p>"""
    service_network_log_type: NotRequired[
        "capo_vpc_lattice.types.service_network_log_type.ServiceNetworkLogType"
    ]
    """<p>Log type of the service network.</p>"""
    created_at: "capo_vpc_lattice.types.timestamp.Timestamp"
    """<p>The date and time that the access log subscription was created, in ISO-8601 format.</p>"""
    last_updated_at: "capo_vpc_lattice.types.timestamp.Timestamp"
    """<p>The date and time that the access log subscription was last updated, in ISO-8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessLogSubscriptionSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["resourceId"] = value["resource_id"]
    out["resourceArn"] = value["resource_arn"]
    out["destinationArn"] = value["destination_arn"]
    if "service_network_log_type" in value:
        out["serviceNetworkLogType"] = value["service_network_log_type"]
    import capo_vpc_lattice.types.timestamp

    out["createdAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_vpc_lattice.types.timestamp

    out["lastUpdatedAt"] = capo_vpc_lattice.types.timestamp.serialize_json(
        value["last_updated_at"]
    )
    return out


def deserialize_json(data: dict) -> AccessLogSubscriptionSummary:
    out: AccessLogSubscriptionSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AccessLogSubscriptionSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AccessLogSubscriptionSummary.arn required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("AccessLogSubscriptionSummary.resource_id required")
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("AccessLogSubscriptionSummary.resource_arn required")
    if "destinationArn" in data:
        out["destination_arn"] = data["destinationArn"]
    else:
        raise DeserializationError(
            "AccessLogSubscriptionSummary.destination_arn required"
        )
    if "serviceNetworkLogType" in data:
        out["service_network_log_type"] = data["serviceNetworkLogType"]
    if "createdAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["created_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("AccessLogSubscriptionSummary.created_at required")
    if "lastUpdatedAt" in data:
        import capo_vpc_lattice.types.timestamp

        out["last_updated_at"] = capo_vpc_lattice.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    else:
        raise DeserializationError(
            "AccessLogSubscriptionSummary.last_updated_at required"
        )
    return out
