"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CreateJobTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.date
    import aws_sdk_emr_containers.types.job_template_arn
    import aws_sdk_emr_containers.types.resource_id_string
    import aws_sdk_emr_containers.types.resource_name_string


class CreateJobTemplateResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"]
    """<p>This output display the created job template ID.</p>"""
    name: NotRequired[
        "aws_sdk_emr_containers.types.resource_name_string.ResourceNameString"
    ]
    """<p>This output displays the name of the created job template.</p>"""
    arn: NotRequired["aws_sdk_emr_containers.types.job_template_arn.JobTemplateArn"]
    """<p>This output display the ARN of the created job template.</p>"""
    created_at: NotRequired["aws_sdk_emr_containers.types.date.Date"]
    """<p>This output displays the date and time when the job template was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobTemplateResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_emr_containers.types.date

        out["createdAt"] = aws_sdk_emr_containers.types.date.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> CreateJobTemplateResponse:
    out: CreateJobTemplateResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_emr_containers.types.date

        out["created_at"] = aws_sdk_emr_containers.types.date.deserialize_json(
            data["createdAt"]
        )
    return out
