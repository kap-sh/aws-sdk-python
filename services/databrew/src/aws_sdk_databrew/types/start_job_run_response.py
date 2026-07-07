"""Generated from Smithy shape ``com.amazonaws.databrew#StartJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_databrew.types.job_run_id


class StartJobRunResponse(TypedDict, closed=True):
    run_id: "aws_sdk_databrew.types.job_run_id.JobRunId"
    """<p>A system-generated identifier for this particular job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRunResponse) -> dict:
    out: dict = {}
    out["RunId"] = value["run_id"]
    return out


def deserialize_json(data: dict) -> StartJobRunResponse:
    out: StartJobRunResponse = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    else:
        raise DeserializationError("StartJobRunResponse.run_id required")
    return out
