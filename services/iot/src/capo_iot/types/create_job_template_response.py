"""Generated from Smithy shape ``com.amazonaws.iot#CreateJobTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.job_template_arn
    import capo_iot.types.job_template_id


class CreateJobTemplateResponse(TypedDict, closed=True):
    job_template_arn: NotRequired["capo_iot.types.job_template_arn.JobTemplateArn"]
    """<p>The ARN of the job template.</p>"""
    job_template_id: NotRequired["capo_iot.types.job_template_id.JobTemplateId"]
    """<p>The unique identifier of the job template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobTemplateResponse) -> dict:
    out: dict = {}
    if "job_template_arn" in value:
        out["jobTemplateArn"] = value["job_template_arn"]
    if "job_template_id" in value:
        out["jobTemplateId"] = value["job_template_id"]
    return out


def deserialize_json(data: dict) -> CreateJobTemplateResponse:
    out: CreateJobTemplateResponse = {}  # type: ignore[typeddict-item]
    if "jobTemplateArn" in data:
        out["job_template_arn"] = data["jobTemplateArn"]
    if "jobTemplateId" in data:
        out["job_template_id"] = data["jobTemplateId"]
    return out
