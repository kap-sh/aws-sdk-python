"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteVpcEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.delete_vpc_endpoint_detail


class DeleteVpcEndpointResponse(TypedDict):
    delete_vpc_endpoint_detail: NotRequired[
        "aws_sdk_opensearchserverless.types.delete_vpc_endpoint_detail.DeleteVpcEndpointDetail"
    ]
    """<p>Details about the deleted endpoint.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVpcEndpointResponse) -> dict:
    out: dict = {}
    if "delete_vpc_endpoint_detail" in value:
        import aws_sdk_opensearchserverless.types.delete_vpc_endpoint_detail

        out["deleteVpcEndpointDetail"] = (
            aws_sdk_opensearchserverless.types.delete_vpc_endpoint_detail.serialize_aws_json_1_0(
                value["delete_vpc_endpoint_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVpcEndpointResponse:
    out: DeleteVpcEndpointResponse = {}  # type: ignore[typeddict-item]
    if "deleteVpcEndpointDetail" in data:
        import aws_sdk_opensearchserverless.types.delete_vpc_endpoint_detail

        out["delete_vpc_endpoint_detail"] = (
            aws_sdk_opensearchserverless.types.delete_vpc_endpoint_detail.deserialize_aws_json_1_0(
                data["deleteVpcEndpointDetail"]
            )
        )
    return out
