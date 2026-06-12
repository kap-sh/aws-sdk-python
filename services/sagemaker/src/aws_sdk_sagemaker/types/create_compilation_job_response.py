"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateCompilationJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.compilation_job_arn


class CreateCompilationJobResponse(TypedDict):
    compilation_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.compilation_job_arn.CompilationJobArn"
    ]
    """<p>If the action is successful, the service sends back an HTTP 200 response. Amazon SageMaker AI returns the following data in JSON format:</p> <ul> <li> <p> <code>CompilationJobArn</code>: The Amazon Resource Name (ARN) of the compiled job.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCompilationJobResponse) -> dict:
    out: dict = {}
    if "compilation_job_arn" in value:
        out["CompilationJobArn"] = value["compilation_job_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCompilationJobResponse:
    out: CreateCompilationJobResponse = {}  # type: ignore[typeddict-item]
    if "CompilationJobArn" in data:
        out["compilation_job_arn"] = data["CompilationJobArn"]
    return out
