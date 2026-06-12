"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#CreateJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.job


class CreateJobResponse(TypedDict):
    job: NotRequired["aws_sdk_elastic_transcoder.types.job.Job"]
    """<p>A section of the response body that provides information about the job that is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import aws_sdk_elastic_transcoder.types.job

        out["Job"] = aws_sdk_elastic_transcoder.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> CreateJobResponse:
    out: CreateJobResponse = {}  # type: ignore[typeddict-item]
    if "Job" in data:
        import aws_sdk_elastic_transcoder.types.job

        out["job"] = aws_sdk_elastic_transcoder.types.job.deserialize_json(data["Job"])
    return out
