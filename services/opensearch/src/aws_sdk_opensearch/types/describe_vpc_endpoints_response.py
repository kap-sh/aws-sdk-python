"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeVpcEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.vpc_endpoint_error_list
    import aws_sdk_opensearch.types.vpc_endpoints


class DescribeVpcEndpointsResponse(TypedDict):
    vpc_endpoints: "aws_sdk_opensearch.types.vpc_endpoints.VpcEndpoints"
    """<p>Information about each requested VPC endpoint.</p>"""
    vpc_endpoint_errors: (
        "aws_sdk_opensearch.types.vpc_endpoint_error_list.VpcEndpointErrorList"
    )
    """<p>Any errors associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVpcEndpointsResponse) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.vpc_endpoints

    out["VpcEndpoints"] = aws_sdk_opensearch.types.vpc_endpoints.serialize_json(
        value["vpc_endpoints"]
    )
    import aws_sdk_opensearch.types.vpc_endpoint_error_list

    out["VpcEndpointErrors"] = (
        aws_sdk_opensearch.types.vpc_endpoint_error_list.serialize_json(
            value["vpc_endpoint_errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeVpcEndpointsResponse:
    out: DescribeVpcEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "VpcEndpoints" in data:
        import aws_sdk_opensearch.types.vpc_endpoints

        out["vpc_endpoints"] = aws_sdk_opensearch.types.vpc_endpoints.deserialize_json(
            data["VpcEndpoints"]
        )
    else:
        raise DeserializationError(
            "DescribeVpcEndpointsResponse.vpc_endpoints required"
        )
    if "VpcEndpointErrors" in data:
        import aws_sdk_opensearch.types.vpc_endpoint_error_list

        out["vpc_endpoint_errors"] = (
            aws_sdk_opensearch.types.vpc_endpoint_error_list.deserialize_json(
                data["VpcEndpointErrors"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeVpcEndpointsResponse.vpc_endpoint_errors required"
        )
    return out
