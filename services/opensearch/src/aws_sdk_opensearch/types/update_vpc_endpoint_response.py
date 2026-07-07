"""Generated from Smithy shape ``com.amazonaws.opensearch#UpdateVpcEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.vpc_endpoint


class UpdateVpcEndpointResponse(TypedDict, closed=True):
    vpc_endpoint: "aws_sdk_opensearch.types.vpc_endpoint.VpcEndpoint"
    """<p>The endpoint to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVpcEndpointResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.vpc_endpoint

    out["VpcEndpoint"] = aws_sdk_opensearch.types.vpc_endpoint.serialize_json(
        value["vpc_endpoint"]
    )
    return out


def deserialize_json(data: dict) -> UpdateVpcEndpointResponse:
    out: UpdateVpcEndpointResponse = {}  # type: ignore[typeddict-item]
    if "VpcEndpoint" in data:
        import aws_sdk_opensearch.types.vpc_endpoint

        out["vpc_endpoint"] = aws_sdk_opensearch.types.vpc_endpoint.deserialize_json(
            data["VpcEndpoint"]
        )
    else:
        raise DeserializationError("UpdateVpcEndpointResponse.vpc_endpoint required")
    return out
