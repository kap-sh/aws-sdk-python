"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DeleteVirtualClusterRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string


class DeleteVirtualClusterRequest(TypedDict):
    id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the virtual cluster that will be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVirtualClusterRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVirtualClusterRequest:
    out: DeleteVirtualClusterRequest = {}  # type: ignore[typeddict-item]
    return out
