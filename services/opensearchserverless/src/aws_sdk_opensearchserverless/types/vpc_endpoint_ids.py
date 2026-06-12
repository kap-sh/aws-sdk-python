"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#VpcEndpointIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_id

VpcEndpointIds: TypeAlias = list[
    "aws_sdk_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointIds) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> VpcEndpointIds:
    return list(data)
