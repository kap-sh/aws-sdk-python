"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateModelInvocationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.model_invocation_job_arn


class CreateModelInvocationJobResponse(TypedDict, closed=True):
    job_arn: "capo_bedrock.types.model_invocation_job_arn.ModelInvocationJobArn"
    """<p>The Amazon Resource Name (ARN) of the batch inference job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelInvocationJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    return out


def deserialize_json(data: dict) -> CreateModelInvocationJobResponse:
    out: CreateModelInvocationJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("CreateModelInvocationJobResponse.job_arn required")
    return out
