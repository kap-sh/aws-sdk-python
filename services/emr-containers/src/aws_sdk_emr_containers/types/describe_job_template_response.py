"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DescribeJobTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.job_template


class DescribeJobTemplateResponse(TypedDict):
    job_template: NotRequired["aws_sdk_emr_containers.types.job_template.JobTemplate"]
    """<p>This output displays information about the specified job template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobTemplateResponse) -> dict:
    out: dict = {}
    if "job_template" in value:
        import aws_sdk_emr_containers.types.job_template

        out["jobTemplate"] = aws_sdk_emr_containers.types.job_template.serialize_json(
            value["job_template"]
        )
    return out


def deserialize_json(data: dict) -> DescribeJobTemplateResponse:
    out: DescribeJobTemplateResponse = {}  # type: ignore[typeddict-item]
    if "jobTemplate" in data:
        import aws_sdk_emr_containers.types.job_template

        out["job_template"] = (
            aws_sdk_emr_containers.types.job_template.deserialize_json(
                data["jobTemplate"]
            )
        )
    return out
