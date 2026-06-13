"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateModelCopyJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_copy_job_arn


class CreateModelCopyJobResponse(TypedDict):
    job_arn: "aws_sdk_bedrock.types.model_copy_job_arn.ModelCopyJobArn"
    """<p>The Amazon Resource Name (ARN) of the model copy job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelCopyJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    return out


def deserialize_json(data: dict) -> CreateModelCopyJobResponse:
    out: CreateModelCopyJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("CreateModelCopyJobResponse.job_arn required")
    return out
