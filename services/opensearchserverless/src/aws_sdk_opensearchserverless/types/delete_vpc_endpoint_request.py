"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteVpcEndpointRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.client_token
    import aws_sdk_opensearchserverless.types.vpc_endpoint_id


class DeleteVpcEndpointRequest(TypedDict):
    id: "aws_sdk_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId"
    """<p>The VPC endpoint identifier.</p>"""
    client_token: NotRequired[
        "aws_sdk_opensearchserverless.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVpcEndpointRequest) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVpcEndpointRequest:
    out: DeleteVpcEndpointRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteVpcEndpointRequest.id required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
