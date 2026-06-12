"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GetJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.job


class GetJobResponse(TypedDict):
    job: NotRequired["aws_sdk_mediaconvert.types.job.Job"]
    """Each job converts an input file into an output file or files. For more information, see the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import aws_sdk_mediaconvert.types.job

        out["job"] = aws_sdk_mediaconvert.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> GetJobResponse:
    out: GetJobResponse = {}  # type: ignore[typeddict-item]
    if "job" in data:
        import aws_sdk_mediaconvert.types.job

        out["job"] = aws_sdk_mediaconvert.types.job.deserialize_json(data["job"])
    return out
