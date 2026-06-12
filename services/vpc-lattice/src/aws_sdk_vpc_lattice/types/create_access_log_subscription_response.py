"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateAccessLogSubscriptionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.access_log_destination_arn
    import aws_sdk_vpc_lattice.types.access_log_subscription_arn
    import aws_sdk_vpc_lattice.types.access_log_subscription_id
    import aws_sdk_vpc_lattice.types.resource_arn
    import aws_sdk_vpc_lattice.types.resource_id
    import aws_sdk_vpc_lattice.types.service_network_log_type


class CreateAccessLogSubscriptionResponse(TypedDict):
    id: "aws_sdk_vpc_lattice.types.access_log_subscription_id.AccessLogSubscriptionId"
    """<p>The ID of the access log subscription.</p>"""
    arn: (
        "aws_sdk_vpc_lattice.types.access_log_subscription_arn.AccessLogSubscriptionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the access log subscription.</p>"""
    resource_id: "aws_sdk_vpc_lattice.types.resource_id.ResourceId"
    """<p>The ID of the service network or service.</p>"""
    resource_arn: "aws_sdk_vpc_lattice.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the service network or service.</p>"""
    service_network_log_type: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_log_type.ServiceNetworkLogType"
    ]
    """<p>The type of log that monitors your Amazon VPC Lattice service networks.</p>"""
    destination_arn: (
        "aws_sdk_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the log destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessLogSubscriptionResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["resourceId"] = value["resource_id"]
    out["resourceArn"] = value["resource_arn"]
    if "service_network_log_type" in value:
        out["serviceNetworkLogType"] = value["service_network_log_type"]
    out["destinationArn"] = value["destination_arn"]
    return out


def deserialize_json(data: dict) -> CreateAccessLogSubscriptionResponse:
    out: CreateAccessLogSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateAccessLogSubscriptionResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateAccessLogSubscriptionResponse.arn required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError(
            "CreateAccessLogSubscriptionResponse.resource_id required"
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "CreateAccessLogSubscriptionResponse.resource_arn required"
        )
    if "serviceNetworkLogType" in data:
        out["service_network_log_type"] = data["serviceNetworkLogType"]
    if "destinationArn" in data:
        out["destination_arn"] = data["destinationArn"]
    else:
        raise DeserializationError(
            "CreateAccessLogSubscriptionResponse.destination_arn required"
        )
    return out
