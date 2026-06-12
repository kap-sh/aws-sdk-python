"""Generated from Smithy shape ``com.amazonaws.databrew#StopJobRunResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.job_run_id


class StopJobRunResponse(TypedDict):
    run_id: "aws_sdk_databrew.types.job_run_id.JobRunId"
    """<p>The ID of the job run that you stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopJobRunResponse) -> dict:
    out: dict = {}
    out["RunId"] = value["run_id"]
    return out


def deserialize_json(data: dict) -> StopJobRunResponse:
    out: StopJobRunResponse = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("StopJobRunResponse.run_id required")
    return out
