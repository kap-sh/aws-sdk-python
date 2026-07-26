"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeCompilationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name


class DescribeCompilationJobRequest(TypedDict, closed=True):
    compilation_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the model compilation job that you want information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCompilationJobRequest) -> dict:
    out: dict = {}
    if "compilation_job_name" in value:
        out["CompilationJobName"] = value["compilation_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCompilationJobRequest:
    out: DescribeCompilationJobRequest = {}  # type: ignore[typeddict-item]
    if "CompilationJobName" in data:
        out["compilation_job_name"] = data["CompilationJobName"]
    return out
