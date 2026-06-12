"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateVirtualClusterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string
    import aws_sdk_emr_containers.types.resource_name_string
    import aws_sdk_emr_containers.types.virtual_cluster_arn


class CreateVirtualClusterResponse(TypedDict):
    id: NotRequired["aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>This output contains the virtual cluster ID.</p>"""
    name: NotRequired[
        "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>This output contains the name of the virtual cluster.</p>"""
    arn: NotRequired[
        "aws_sdk_emr_containers.types.virtual_cluster_arn.VirtualClusterArn"
    ]
    """<p>This output contains the ARN of virtual cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVirtualClusterResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateVirtualClusterResponse:
    out: CreateVirtualClusterResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
