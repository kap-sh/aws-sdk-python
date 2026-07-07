"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#ReadJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.job


class ReadJobResponse(TypedDict, closed=True):
    job: NotRequired["aws_sdk_elastic_transcoder.types.job.Job"]
    """<p>A section of the response body that provides information about the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadJobResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import aws_sdk_elastic_transcoder.types.job

        out["Job"] = aws_sdk_elastic_transcoder.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> ReadJobResponse:
    out: ReadJobResponse = {}  # type: ignore[typeddict-item]
    if "Job" in data:
        import aws_sdk_elastic_transcoder.types.job

        out["job"] = aws_sdk_elastic_transcoder.types.job.deserialize_json(data["Job"])
    return out
