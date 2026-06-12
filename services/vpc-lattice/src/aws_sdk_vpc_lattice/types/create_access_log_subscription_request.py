"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateAccessLogSubscriptionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.access_log_destination_arn
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.resource_identifier
    import aws_sdk_vpc_lattice.types.service_network_log_type
    import aws_sdk_vpc_lattice.types.tag_map


class CreateAccessLogSubscriptionRequest(TypedDict):
    client_token: NotRequired["aws_sdk_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    resource_identifier: (
        "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The ID or ARN of the service network or service.</p>"""
    destination_arn: (
        "aws_sdk_vpc_lattice.types.access_log_destination_arn.AccessLogDestinationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the destination. The supported destination types are CloudWatch Log groups, Kinesis Data Firehose delivery streams, and Amazon S3 buckets.</p>"""
    service_network_log_type: NotRequired[
        "aws_sdk_vpc_lattice.types.service_network_log_type.ServiceNetworkLogType"
    ]
    """<p>The type of log that monitors your Amazon VPC Lattice service networks.</p>"""
    tags: NotRequired["aws_sdk_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the access log subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessLogSubscriptionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["resourceIdentifier"] = value["resource_identifier"]
    out["destinationArn"] = value["destination_arn"]
    if "service_network_log_type" in value:
        out["serviceNetworkLogType"] = value["service_network_log_type"]
    if "tags" in value:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAccessLogSubscriptionRequest:
    out: CreateAccessLogSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "resourceIdentifier" in data:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        raise DeserializationError(
            "CreateAccessLogSubscriptionRequest.resource_identifier required"
        )
    if "destinationArn" in data:
        out["destination_arn"] = data["destinationArn"]
    else:
        raise DeserializationError(
            "CreateAccessLogSubscriptionRequest.destination_arn required"
        )
    if "serviceNetworkLogType" in data:
        out["service_network_log_type"] = data["serviceNetworkLogType"]
    if "tags" in data:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
