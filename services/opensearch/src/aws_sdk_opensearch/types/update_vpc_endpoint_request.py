"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateVpcEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.vpc_endpoint_id
    import aws_sdk_opensearch.types.vpc_options


class UpdateVpcEndpointRequest(TypedDict):
    vpc_endpoint_id: "aws_sdk_opensearch.types.vpc_endpoint_id.VpcEndpointId"
    """<p>The unique identifier of the endpoint.</p>"""
    vpc_options: "aws_sdk_opensearch.types.vpc_options.VPCOptions"
    """<p>The security groups and/or subnets to add, remove, or modify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVpcEndpointRequest) -> dict:
    out: dict = {}
    out["VpcEndpointId"] = value["vpc_endpoint_id"]
    import aws_sdk_opensearch.types.vpc_options

    out["VpcOptions"] = aws_sdk_opensearch.types.vpc_options.serialize_json(
        value["vpc_options"]
    )
    return out


def deserialize_json(data: dict) -> UpdateVpcEndpointRequest:
    out: UpdateVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    else:
        raise DeserializationError("UpdateVpcEndpointRequest.vpc_endpoint_id required")
    if "VpcOptions" in data:
        import aws_sdk_opensearch.types.vpc_options

        out["vpc_options"] = aws_sdk_opensearch.types.vpc_options.deserialize_json(
            data["VpcOptions"]
        )
    else:
        raise DeserializationError("UpdateVpcEndpointRequest.vpc_options required")
    return out
