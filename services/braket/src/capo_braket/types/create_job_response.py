"""Generated from Smithy shape ``com.amazonaws.braket#CreateJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_braket.errors import DeserializationError

if TYPE_CHECKING:
    import capo_braket.types.job_arn


class CreateJobResponse(TypedDict, closed=True):
    job_arn: "capo_braket.types.job_arn.JobArn"
    """<p>The ARN of the Amazon Braket hybrid job created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    return out


def deserialize_json(data: dict) -> CreateJobResponse:
    out: CreateJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("CreateJobResponse.job_arn required")
    return out
