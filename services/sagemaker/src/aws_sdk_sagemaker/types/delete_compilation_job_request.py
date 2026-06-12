"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteCompilationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class DeleteCompilationJobRequest(TypedDict):
    compilation_job_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the compilation job to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCompilationJobRequest) -> dict:
    out: dict = {}
    if "compilation_job_name" in value:
        out["CompilationJobName"] = value["compilation_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCompilationJobRequest:
    out: DeleteCompilationJobRequest = {}  # type: ignore[typeddict-item]
    if "CompilationJobName" in data:
        out["compilation_job_name"] = data["CompilationJobName"]
    return out
