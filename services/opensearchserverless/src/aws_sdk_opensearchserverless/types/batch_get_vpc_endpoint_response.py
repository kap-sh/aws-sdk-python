"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetVpcEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_details
    import aws_sdk_opensearchserverless.types.vpc_endpoint_error_details


class BatchGetVpcEndpointResponse(TypedDict, closed=True):
    vpc_endpoint_details: NotRequired[
        "aws_sdk_opensearchserverless.types.vpc_endpoint_details.VpcEndpointDetails"
    ]
    """<p>Details about the specified VPC endpoint.</p>"""
    vpc_endpoint_error_details: NotRequired[
        "aws_sdk_opensearchserverless.types.vpc_endpoint_error_details.VpcEndpointErrorDetails"
    ]
    """<p>Error information for a failed request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetVpcEndpointResponse) -> dict:
    out: dict = {}
    if "vpc_endpoint_details" in value:
        import aws_sdk_opensearchserverless.types.vpc_endpoint_details

        out["vpcEndpointDetails"] = (
            aws_sdk_opensearchserverless.types.vpc_endpoint_details.serialize_aws_json_1_0(
                value["vpc_endpoint_details"]
            )
        )
    if "vpc_endpoint_error_details" in value:
        import aws_sdk_opensearchserverless.types.vpc_endpoint_error_details

        out["vpcEndpointErrorDetails"] = (
            aws_sdk_opensearchserverless.types.vpc_endpoint_error_details.serialize_aws_json_1_0(
                value["vpc_endpoint_error_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetVpcEndpointResponse:
    out: BatchGetVpcEndpointResponse = {}  # type: ignore[typeddict-item]
    if "vpcEndpointDetails" in data:
        import aws_sdk_opensearchserverless.types.vpc_endpoint_details

        out["vpc_endpoint_details"] = (
            aws_sdk_opensearchserverless.types.vpc_endpoint_details.deserialize_aws_json_1_0(
                data["vpcEndpointDetails"]
            )
        )
    if "vpcEndpointErrorDetails" in data:
        import aws_sdk_opensearchserverless.types.vpc_endpoint_error_details

        out["vpc_endpoint_error_details"] = (
            aws_sdk_opensearchserverless.types.vpc_endpoint_error_details.deserialize_aws_json_1_0(
                data["vpcEndpointErrorDetails"]
            )
        )
    return out
