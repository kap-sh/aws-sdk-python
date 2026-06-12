"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopCompilationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class StopCompilationJobRequest(TypedDict):
    compilation_job_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model compilation job to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopCompilationJobRequest) -> dict:
    out: dict = {}
    if "compilation_job_name" in value:
        out["CompilationJobName"] = value["compilation_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopCompilationJobRequest:
    out: StopCompilationJobRequest = {}  # type: ignore[typeddict-item]
    if "CompilationJobName" in data:
        out["compilation_job_name"] = data["CompilationJobName"]
    return out
