"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CreateJobTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.job_template


class CreateJobTemplateResponse(TypedDict, closed=True):
    job_template: NotRequired["capo_mediaconvert.types.job_template.JobTemplate"]
    """A job template is a pre-made set of encoding instructions that you can use to quickly create a job."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobTemplateResponse) -> dict:
    out: dict = {}
    if "job_template" in value:
        import capo_mediaconvert.types.job_template

        out["jobTemplate"] = capo_mediaconvert.types.job_template.serialize_json(
            value["job_template"]
        )
    return out


def deserialize_json(data: dict) -> CreateJobTemplateResponse:
    out: CreateJobTemplateResponse = {}  # type: ignore[typeddict-item]
    if "jobTemplate" in data:
        import capo_mediaconvert.types.job_template

        out["job_template"] = capo_mediaconvert.types.job_template.deserialize_json(
            data["jobTemplate"]
        )
    return out
