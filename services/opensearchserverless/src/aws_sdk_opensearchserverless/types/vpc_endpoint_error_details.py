"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#VpcEndpointErrorDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_error_detail

VpcEndpointErrorDetails: TypeAlias = list[
    "aws_sdk_opensearchserverless.types.vpc_endpoint_error_detail.VpcEndpointErrorDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointErrorDetails) -> list:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_error_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearchserverless.types.vpc_endpoint_error_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VpcEndpointErrorDetails:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_error_detail

    out: VpcEndpointErrorDetails = []
    for item in data:
        out.append(
            aws_sdk_opensearchserverless.types.vpc_endpoint_error_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
