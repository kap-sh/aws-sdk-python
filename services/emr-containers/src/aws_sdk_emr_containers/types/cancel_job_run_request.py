"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CancelJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string


class CancelJobRunRequest(TypedDict, closed=True):
    id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the job run to cancel.</p>"""
    virtual_cluster_id: (
        "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    )
    """<p>The ID of the virtual cluster for which the job run will be canceled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelJobRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelJobRunRequest:
    out: CancelJobRunRequest = {}  # type: ignore[typeddict-item]
    return out
