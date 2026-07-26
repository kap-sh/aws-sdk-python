"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DescribeJobTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.job_template


class DescribeJobTemplateResponse(TypedDict, closed=True):
    job_template: NotRequired["capo_emr_containers.types.job_template.JobTemplate"]
    """<p>This output displays information about the specified job template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobTemplateResponse) -> dict:
    out: dict = {}
    if "job_template" in value:
        import capo_emr_containers.types.job_template

        out["jobTemplate"] = capo_emr_containers.types.job_template.serialize_json(
            value["job_template"]
        )
    return out


def deserialize_json(data: dict) -> DescribeJobTemplateResponse:
    out: DescribeJobTemplateResponse = {}  # type: ignore[typeddict-item]
    if "jobTemplate" in data:
        import capo_emr_containers.types.job_template

        out["job_template"] = capo_emr_containers.types.job_template.deserialize_json(
            data["jobTemplate"]
        )
    return out
