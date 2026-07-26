"""Generated from Smithy shape ``com.amazonaws.iot#JobTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.date_type
    import capo_iot.types.job_description
    import capo_iot.types.job_template_arn
    import capo_iot.types.job_template_id


class JobTemplateSummary(TypedDict, closed=True):
    job_template_arn: NotRequired["capo_iot.types.job_template_arn.JobTemplateArn"]
    """<p>The ARN of the job template.</p>"""
    job_template_id: NotRequired["capo_iot.types.job_template_id.JobTemplateId"]
    """<p>The unique identifier of the job template.</p>"""
    description: NotRequired["capo_iot.types.job_description.JobDescription"]
    """<p>A description of the job template.</p>"""
    created_at: NotRequired["capo_iot.types.date_type.DateType"]
    """<p>The time, in seconds since the epoch, when the job template was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobTemplateSummary) -> dict:
    out: dict = {}
    if "job_template_arn" in value:
        out["jobTemplateArn"] = value["job_template_arn"]
    if "job_template_id" in value:
        out["jobTemplateId"] = value["job_template_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import capo_iot.types.date_type

        out["createdAt"] = capo_iot.types.date_type.serialize_json(value["created_at"])
    return out


def deserialize_json(data: dict) -> JobTemplateSummary:
    out: JobTemplateSummary = {}  # type: ignore[typeddict-item]
    if "jobTemplateArn" in data:
        out["job_template_arn"] = data["jobTemplateArn"]
    if "jobTemplateId" in data:
        out["job_template_id"] = data["jobTemplateId"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import capo_iot.types.date_type

        out["created_at"] = capo_iot.types.date_type.deserialize_json(data["createdAt"])
    return out
