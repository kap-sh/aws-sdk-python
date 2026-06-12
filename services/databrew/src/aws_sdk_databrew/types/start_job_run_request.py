"""Generated from Smithy shape ``com.amazonaws.databrew#StartJobRunRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.job_name


class StartJobRunRequest(TypedDict):
    name: "aws_sdk_databrew.types.job_name.JobName"
    """<p>The name of the job to be run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartJobRunRequest:
    out: StartJobRunRequest = {}  # type: ignore[typeddict-item]
    return out
