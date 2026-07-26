"""Generated from Smithy shape ``com.amazonaws.emrcontainers#StartJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.job_arn
    import capo_emr_containers.types.resource_id_string
    import capo_emr_containers.types.resource_name_string


class StartJobRunResponse(TypedDict, closed=True):
    id: NotRequired["capo_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>This output displays the started job run ID.</p>"""
    name: NotRequired[
        "capo_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>This output displays the name of the started job run.</p>"""
    arn: NotRequired["capo_emr_containers.types.job_arn.JobArn"]
    """<p>This output lists the ARN of job run.</p>"""
    virtual_cluster_id: NotRequired[
        "capo_emr_containers.types.resource_id_string.ResourceIdString"
    ]
    """<p>This output displays the virtual cluster ID for which the job run was submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRunResponse) -> dict:
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


def deserialize_json(data: dict) -> StartJobRunResponse:
    out: StartJobRunResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "virtualClusterId" in data:
        out["virtual_cluster_id"] = data["virtualClusterId"]
    return out
