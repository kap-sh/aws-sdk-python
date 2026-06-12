"""Generated from Smithy shape ``com.amazonaws.vpclattice#UpdateAccessLogSubscriptionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.access_log_destination_arn
    import aws_sdk_vpc_lattice.types.access_log_subscription_arn
    import aws_sdk_vpc_lattice.types.access_log_subscription_id
    import aws_sdk_vpc_lattice.types.resource_arn
    import aws_sdk_vpc_lattice.types.resource_id


class UpdateAccessLogSubscriptionResponse(TypedDict):
    id: "aws_sdk_vpc_lattice.types.access_log_subscription_id.AccessLogSubscriptionId"
    """<p>The ID of the access log subscription.</p>"""
    arn: (
        "aws_sdk_vpc_lattice.types.access_log_subscription_arn.AccessLogSubscriptionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the access log subscription.</p>"""
    resource_id: "aws_sdk_vpc_lattice.types.resource_id.ResourceId"
    """<p>The ID of the resource.</p>"""
    resource_arn: "aws_sdk_vpc_lattice.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the access log subscription.</p>"""
    destination_arn: (
        "aws_sdk_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the access log destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessLogSubscriptionResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["resourceId"] = value["resource_id"]
    out["resourceArn"] = value["resource_arn"]
    out["destinationArn"] = value["destination_arn"]
    return out


def deserialize_json(data: dict) -> UpdateAccessLogSubscriptionResponse:
    out: UpdateAccessLogSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateAccessLogSubscriptionResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateAccessLogSubscriptionResponse.arn required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError(
            "UpdateAccessLogSubscriptionResponse.resource_id required"
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "UpdateAccessLogSubscriptionResponse.resource_arn required"
        )
    if "destinationArn" in data:
        out["destination_arn"] = data["destinationArn"]
    else:
        raise DeserializationError(
            "UpdateAccessLogSubscriptionResponse.destination_arn required"
        )
    return out
