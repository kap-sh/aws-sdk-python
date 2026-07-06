"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateCustomRoutingEndpointGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.custom_routing_destination_configurations
    import aws_sdk_global_accelerator.types.generic_string
    import aws_sdk_global_accelerator.types.idempotency_token


class CreateCustomRoutingEndpointGroupRequest(TypedDict, closed=True):
    listener_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the listener for a custom routing endpoint.</p>"""
    endpoint_group_region: (
        "aws_sdk_global_accelerator.types.generic_string.GenericString"
    )
    """<p>The Amazon Web Services Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.</p>"""
    destination_configurations: "aws_sdk_global_accelerator.types.custom_routing_destination_configurations.CustomRoutingDestinationConfigurations"
    """<p>Sets the port range and protocol for all endpoints (virtual private cloud subnets) in a custom routing endpoint group to accept client traffic on.</p>"""
    idempotency_token: (
        "aws_sdk_global_accelerator.types.idempotency_token.IdempotencyToken"
    )
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCustomRoutingEndpointGroupRequest) -> dict:
    out: dict = {}
    out["ListenerArn"] = value["listener_arn"]
    out["EndpointGroupRegion"] = value["endpoint_group_region"]
    import aws_sdk_global_accelerator.types.custom_routing_destination_configurations

    out["DestinationConfigurations"] = (
        aws_sdk_global_accelerator.types.custom_routing_destination_configurations.serialize_aws_json_1_1(
            value["destination_configurations"]
        )
    )
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCustomRoutingEndpointGroupRequest:
    out: CreateCustomRoutingEndpointGroupRequest = {}  # type: ignore[typeddict-item]
    if "ListenerArn" in data:
        out["listener_arn"] = data["ListenerArn"]
    else:
        raise DeserializationError(
            "CreateCustomRoutingEndpointGroupRequest.listener_arn required"
        )
    if "EndpointGroupRegion" in data:
        out["endpoint_group_region"] = data["EndpointGroupRegion"]
    else:
        raise DeserializationError(
            "CreateCustomRoutingEndpointGroupRequest.endpoint_group_region required"
        )
    if "DestinationConfigurations" in data:
        import aws_sdk_global_accelerator.types.custom_routing_destination_configurations

        out["destination_configurations"] = (
            aws_sdk_global_accelerator.types.custom_routing_destination_configurations.deserialize_aws_json_1_1(
                data["DestinationConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCustomRoutingEndpointGroupRequest.destination_configurations required"
        )
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "CreateCustomRoutingEndpointGroupRequest.idempotency_token required"
        )
    return out
