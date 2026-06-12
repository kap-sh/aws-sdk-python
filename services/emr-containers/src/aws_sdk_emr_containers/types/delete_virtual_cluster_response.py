"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DeleteVirtualClusterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string


class DeleteVirtualClusterResponse(TypedDict):
    id: NotRequired["aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>This output contains the ID of the virtual cluster that will be deleted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVirtualClusterResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> DeleteVirtualClusterResponse:
    out: DeleteVirtualClusterResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
