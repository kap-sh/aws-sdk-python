"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CreateJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.job


class CreateJobResponse(TypedDict, closed=True):
    job: NotRequired["capo_mediaconvert.types.job.Job"]
    """Each job converts an input file into an output file or files. For more information, see the User Guide at https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import capo_mediaconvert.types.job

        out["job"] = capo_mediaconvert.types.job.serialize_json(value["job"])
    return out


def deserialize_json(data: dict) -> CreateJobResponse:
    out: CreateJobResponse = {}  # type: ignore[typeddict-item]
    if "job" in data:
        import capo_mediaconvert.types.job

        out["job"] = capo_mediaconvert.types.job.deserialize_json(data["job"])
    return out
