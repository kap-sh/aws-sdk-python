"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.job_name


class DeleteJobRequest(TypedDict):
    name: "aws_sdk_databrew.types.job_name.JobName"
    """<p>The name of the job to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteJobRequest:
    out: DeleteJobRequest = {}  # type: ignore[typeddict-item]
    return out
