"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CancelJobRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string


class CancelJobRunResponse(TypedDict):
    id: NotRequired["aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>The output contains the ID of the cancelled job run.</p>"""
    virtual_cluster_id: NotRequired[
        "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    ]
    """<p>The output contains the virtual cluster ID for which the job run is cancelled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRunResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "virtual_cluster_id" in value:
        out["virtualClusterId"] = value["virtual_cluster_id"]
    return out


def deserialize_json(data: dict) -> CancelJobRunResponse:
    out: CancelJobRunResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "virtualClusterId" in data:
        out["virtual_cluster_id"] = data["virtualClusterId"]
    return out
