"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateManagedEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.endpoint_arn
    import aws_sdk_emr_containers.types.resource_id_string
    import aws_sdk_emr_containers.types.resource_name_string


class CreateManagedEndpointResponse(TypedDict):
    id: NotRequired["aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The output contains the ID of the managed endpoint.</p>"""
    name: NotRequired[
        "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>The output contains the name of the managed endpoint.</p>"""
    arn: NotRequired["aws_sdk_emr_containers.types.endpoint_arn.EndpointArn"]
    """<p>The output contains the ARN of the managed endpoint.</p>"""
    virtual_cluster_id: NotRequired[
        "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    ]
    """<p>The output contains the ID of the virtual cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateManagedEndpointResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "virtual_cluster_id" in value:
        out["virtualClusterId"] = value["virtual_cluster_id"]
    return out


def deserialize_json(data: dict) -> CreateManagedEndpointResponse:
    out: CreateManagedEndpointResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "virtualClusterId" in data:
        out["virtual_cluster_id"] = data["virtualClusterId"]
    return out
