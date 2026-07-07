"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GetJobTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.job_template


class GetJobTemplateResponse(TypedDict, closed=True):
    job_template: NotRequired["aws_sdk_mediaconvert.types.job_template.JobTemplate"]
    """A job template is a pre-made set of encoding instructions that you can use to quickly create a job."""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobTemplateResponse) -> dict:
    out: dict = {}
    if "job_template" in value:
        import aws_sdk_mediaconvert.types.job_template

        out["jobTemplate"] = aws_sdk_mediaconvert.types.job_template.serialize_json(
            value["job_template"]
        )
    return out


def deserialize_json(data: dict) -> GetJobTemplateResponse:
    out: GetJobTemplateResponse = {}  # type: ignore[typeddict-item]
    if "jobTemplate" in data:
        import aws_sdk_mediaconvert.types.job_template

        out["job_template"] = aws_sdk_mediaconvert.types.job_template.deserialize_json(
            data["jobTemplate"]
        )
    return out
