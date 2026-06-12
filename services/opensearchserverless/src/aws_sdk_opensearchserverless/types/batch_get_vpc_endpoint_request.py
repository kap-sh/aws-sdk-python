"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#BatchGetVpcEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_ids


class BatchGetVpcEndpointRequest(TypedDict):
    ids: "aws_sdk_opensearchserverless.types.vpc_endpoint_ids.VpcEndpointIds"
    """<p>A list of VPC endpoint identifiers.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetVpcEndpointRequest) -> dict:
    out: dict = {}
    import aws_sdk_opensearchserverless.types.vpc_endpoint_ids

    out["ids"] = (
        aws_sdk_opensearchserverless.types.vpc_endpoint_ids.serialize_aws_json_1_0(
            value["ids"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetVpcEndpointRequest:
    out: BatchGetVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    if "ids" in data:
        import aws_sdk_opensearchserverless.types.vpc_endpoint_ids

        out["ids"] = (
            aws_sdk_opensearchserverless.types.vpc_endpoint_ids.deserialize_aws_json_1_0(
                data["ids"]
            )
        )
    else:
        raise DeserializationError("BatchGetVpcEndpointRequest.ids required")
    return out
