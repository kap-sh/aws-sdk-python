"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#UpdateVpcEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.update_vpc_endpoint_detail


class UpdateVpcEndpointResponse(TypedDict, closed=True):
    update_vpc_endpoint_detail: NotRequired[
        "aws_sdk_opensearchserverless.types.update_vpc_endpoint_detail.UpdateVpcEndpointDetail"
    ]
    """<p>Details about the updated VPC endpoint.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateVpcEndpointResponse) -> dict:
    out: dict = {}
    if "update_vpc_endpoint_detail" in value:
        import aws_sdk_opensearchserverless.types.update_vpc_endpoint_detail

        out["UpdateVpcEndpointDetail"] = (
            aws_sdk_opensearchserverless.types.update_vpc_endpoint_detail.serialize_aws_json_1_0(
                value["update_vpc_endpoint_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateVpcEndpointResponse:
    out: UpdateVpcEndpointResponse = {}  # type: ignore[typeddict-item]
    if "UpdateVpcEndpointDetail" in data:
        import aws_sdk_opensearchserverless.types.update_vpc_endpoint_detail

        out["update_vpc_endpoint_detail"] = (
            aws_sdk_opensearchserverless.types.update_vpc_endpoint_detail.deserialize_aws_json_1_0(
                data["UpdateVpcEndpointDetail"]
            )
        )
    return out
