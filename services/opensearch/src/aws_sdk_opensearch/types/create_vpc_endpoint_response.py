"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateVpcEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.vpc_endpoint


class CreateVpcEndpointResponse(TypedDict, closed=True):
    vpc_endpoint: "aws_sdk_opensearch.types.vpc_endpoint.VpcEndpoint"
    """<p>Information about the newly created VPC endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcEndpointResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.vpc_endpoint

    out["VpcEndpoint"] = aws_sdk_opensearch.types.vpc_endpoint.serialize_json(
        value["vpc_endpoint"]
    )
    return out


def deserialize_json(data: dict) -> CreateVpcEndpointResponse:
    out: CreateVpcEndpointResponse = {}  # type: ignore[typeddict-item]
    if "VpcEndpoint" in data:
        import aws_sdk_opensearch.types.vpc_endpoint

        out["vpc_endpoint"] = aws_sdk_opensearch.types.vpc_endpoint.deserialize_json(
            data["VpcEndpoint"]
        )
    else:
        raise DeserializationError("CreateVpcEndpointResponse.vpc_endpoint required")
    return out
