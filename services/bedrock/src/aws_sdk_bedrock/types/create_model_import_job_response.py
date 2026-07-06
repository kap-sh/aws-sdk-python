"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateModelImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_import_job_arn


class CreateModelImportJobResponse(TypedDict, closed=True):
    job_arn: "aws_sdk_bedrock.types.model_import_job_arn.ModelImportJobArn"
    """<p>The Amazon Resource Name (ARN) of the model import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateModelImportJobResponse) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    return out


def deserialize_json(data: dict) -> CreateModelImportJobResponse:
    out: CreateModelImportJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    else:
        raise DeserializationError("CreateModelImportJobResponse.job_arn required")
    return out
