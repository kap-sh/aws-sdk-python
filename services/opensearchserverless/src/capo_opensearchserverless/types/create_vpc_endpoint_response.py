"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateVpcEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.create_vpc_endpoint_detail


class CreateVpcEndpointResponse(TypedDict, closed=True):
    create_vpc_endpoint_detail: NotRequired[
        "capo_opensearchserverless.types.create_vpc_endpoint_detail.CreateVpcEndpointDetail"
    ]
    """<p>Details about the created interface VPC endpoint.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVpcEndpointResponse) -> dict:
    out: dict = {}
    if "create_vpc_endpoint_detail" in value:
        import capo_opensearchserverless.types.create_vpc_endpoint_detail

        out["createVpcEndpointDetail"] = (
            capo_opensearchserverless.types.create_vpc_endpoint_detail.serialize_aws_json_1_0(
                value["create_vpc_endpoint_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVpcEndpointResponse:
    out: CreateVpcEndpointResponse = {}  # type: ignore[typeddict-item]
    if "createVpcEndpointDetail" in data:
        import capo_opensearchserverless.types.create_vpc_endpoint_detail

        out["create_vpc_endpoint_detail"] = (
            capo_opensearchserverless.types.create_vpc_endpoint_detail.deserialize_aws_json_1_0(
                data["createVpcEndpointDetail"]
            )
        )
    return out
