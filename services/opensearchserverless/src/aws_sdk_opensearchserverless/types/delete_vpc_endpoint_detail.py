"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#DeleteVpcEndpointDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.vpc_endpoint_id
    import aws_sdk_opensearchserverless.types.vpc_endpoint_name
    import aws_sdk_opensearchserverless.types.vpc_endpoint_status


class DeleteVpcEndpointDetail(TypedDict, closed=True):
    id: NotRequired["aws_sdk_opensearchserverless.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The unique identifier of the endpoint.</p>"""
    name: NotRequired[
        "aws_sdk_opensearchserverless.types.vpc_endpoint_name.VpcEndpointName"
    ]
    """<p>The name of the endpoint.</p>"""
    status: NotRequired[
        "aws_sdk_opensearchserverless.types.vpc_endpoint_status.VpcEndpointStatus"
    ]
    """<p>The current status of the endpoint deletion process.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVpcEndpointDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVpcEndpointDetail:
    out: DeleteVpcEndpointDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    return out
