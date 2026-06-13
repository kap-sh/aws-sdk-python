"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetMatchingJobInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.job_id


class GetMatchingJobInput(TypedDict):
    workflow_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""
    job_id: "aws_sdk_entityresolution.types.job_id.JobId"
    """<p>The ID of the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMatchingJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMatchingJobInput:
    out: GetMatchingJobInput = {}  # type: ignore[typeddict-item]
    return out
