"""Generated from Smithy shape ``com.amazonaws.pipes#BatchJobDependency``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pipes.types.batch_job_dependency_type


class BatchJobDependency(TypedDict):
    job_id: NotRequired["str"]
    """<p>The job ID of the Batch job that's associated with this dependency.</p>"""
    type: NotRequired[
        "aws_sdk_pipes.types.batch_job_dependency_type.BatchJobDependencyType"
    ]
    """<p>The type of the job dependency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchJobDependency) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> BatchJobDependency:
    out: BatchJobDependency = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
