"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#VpcEndpointDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearchserverless.types.vpc_endpoint_detail

VpcEndpointDetails: TypeAlias = list[
    "capo_opensearchserverless.types.vpc_endpoint_detail.VpcEndpointDetail"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointDetails) -> list:
    import capo_opensearchserverless.types.vpc_endpoint_detail

    out: list = []
    for item in value:
        out.append(
            capo_opensearchserverless.types.vpc_endpoint_detail.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VpcEndpointDetails:
    import capo_opensearchserverless.types.vpc_endpoint_detail

    out: VpcEndpointDetails = []
    for item in data:
        out.append(
            capo_opensearchserverless.types.vpc_endpoint_detail.deserialize_aws_json_1_0(
                item
            )
        )
    return out
