"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DescribeJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.resource_id_string


class DescribeJobRunRequest(TypedDict, closed=True):
    id: "capo_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the job run request. </p>"""
    virtual_cluster_id: "capo_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the virtual cluster for which the job run is submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeJobRunRequest:
    out: DescribeJobRunRequest = {}  # type: ignore[typeddict-item]
    return out
