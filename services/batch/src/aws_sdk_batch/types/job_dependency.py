"""Generated from Smithy shape ``com.amazonaws.batch#JobDependency``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.array_job_dependency
    import aws_sdk_batch.types.string


class JobDependency(TypedDict):
    job_id: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The job ID of the Batch job that's associated with this dependency.</p>"""
    type: NotRequired["aws_sdk_batch.types.array_job_dependency.ArrayJobDependency"]
    """<p>The type of the job dependency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobDependency) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobId"] = value["job_id"]
    if "type" in value:
        import aws_sdk_batch.types.array_job_dependency

        out["type"] = aws_sdk_batch.types.array_job_dependency.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> JobDependency:
    out: JobDependency = {}  # type: ignore[typeddict-item]
    if "jobId" in data:
        out["job_id"] = data["jobId"]
    if "type" in data:
        import aws_sdk_batch.types.array_job_dependency

        out["type"] = aws_sdk_batch.types.array_job_dependency.deserialize_json(
            data["type"]
        )
    return out
