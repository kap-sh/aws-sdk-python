"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#VpcEndpointDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_detail

VpcEndpointDetails: TypeAlias = list[
    "aws_sdk_opensearchserverless.types.vpc_endpoint_detail.VpcEndpointDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointDetails) -> list:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearchserverless.types.vpc_endpoint_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VpcEndpointDetails:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_detail

    out: VpcEndpointDetails = []
    for item in data:
        out.append(
            aws_sdk_opensearchserverless.types.vpc_endpoint_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
