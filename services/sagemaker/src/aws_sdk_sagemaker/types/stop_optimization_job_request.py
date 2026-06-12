"""Generated from Smithy shape ``com.amazonaws.sagemaker#StopOptimizationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name


class StopOptimizationJobRequest(TypedDict):
    optimization_job_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name that you assigned to the optimization job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopOptimizationJobRequest) -> dict:
    out: dict = {}
    if "optimization_job_name" in value:
        out["OptimizationJobName"] = value["optimization_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopOptimizationJobRequest:
    out: StopOptimizationJobRequest = {}  # type: ignore[typeddict-item]
    if "OptimizationJobName" in data:
        out["optimization_job_name"] = data["OptimizationJobName"]
    return out
